import pkg_resources

from delb import Document


def test_custom_loader():
    url = "remote://the_book_of_brian.xml"
    document = Document(url)

    root = document.root
    assert root.local_name == "document"
    assert root["url"] == url


def test_header_properties():
    document = Document(
        "https://textgridlab.org/1.0/tgcrud-public/rest/textgrid:1265r.0/data"
    )

    assert document.tei_header.title == "Das erste dadaistische Manifest"
    assert document.tei_header.authors == ["Ball, Hugo"]


if __name__ == "__main__":
    try:
        pkg_resources.get_distribution("delb-reference-plugins")
    except pkg_resources.DistributionNotFound:
        print(
            "The package that includes the extensions must be installed in order to "
            "use these."
        )
        raise SystemExit(1)

    test_custom_loader()
    test_header_properties()
    print("Everything worked as expected.")
