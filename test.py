from __future__ import annotations

import warnings
from importlib import metadata
from types import SimpleNamespace

from delb import Document
from delb.typing import TagNodeType


OFFICE_NS = "urn:oasis:names:tc:opendocument:xmlns:office:1.0"
ODT_MIMETYPE = "application/vnd.oasis.opendocument.text"


class OpenDocumentText(Document):
    @staticmethod
    def __class_test__(root: TagNodeType, config: SimpleNamespace) -> bool:
        if root.namespace != OFFICE_NS:
            return False

        if root.local_name != "document":
            return False

        try:
            return root.attributes[(OFFICE_NS, "mimetype")] == ODT_MIMETYPE
        except KeyError:
            return False


def test_custom_loader():
    url = "remote://the_book_of_brian.xml"
    root = Document(url).root

    assert root.local_name == "document"
    assert root["url"] == url


def test_header_properties():
    document = Document(
        "https://textgridlab.org/1.0/tgcrud-public/rest/textgrid:1265r.0/data"
    )
    assert document.tei_header.title == "Das erste dadaistische Manifest"
    assert document.tei_header.authors == ["Ball, Hugo"]

    document.config.tei_header.yelling = True
    assert document.tei_header.title == "DAS ERSTE DADAISTISCHE MANIFEST"

    document = Document(
        "https://textgridlab.org/1.0/tgcrud-public/rest/textgrid:1265r.0/data",
        tei_header_yelling=True,
    )
    assert document.tei_header.title == "DAS ERSTE DADAISTISCHE MANIFEST"


def test_subclass():
    stub = f'<document xmlns="{OFFICE_NS}" mimetype="{ODT_MIMETYPE}"/>'
    assert isinstance(Document(stub), OpenDocumentText)

    stub = stub.replace("open", "closed")
    document = Document(stub)
    assert isinstance(document, Document)
    assert not isinstance(document, OpenDocumentText)


if __name__ == "__main__":
    # this isn't trying to import the package as it shall test that delb's loading of
    # entrypoints works
    try:
        metadata.metadata("delb-reference-plugins")
    except metadata.PackageNotFoundError:
        print(
            "The package that includes the extensions must be installed in order to "
            "use these."
        )
        raise SystemExit(1)

    warnings.simplefilter("error")

    test_custom_loader()
    test_header_properties()
    test_subclass()

    # TODO provide and test a custom XPath function example
    # TODO provide and test a parser adapter example

    print("Everything worked as expected.")
