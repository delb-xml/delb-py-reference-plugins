# note that nothing is imported from the top-level `delb` module as it would
# trigger the loading of plugins, yet the plugins in this module hasn't been
# registered yet

from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Dict, Final, TypedDict

from _delb.plugins import DocumentMixinBase

class NamespacesKWArgs(TypedDict):
    namespaces: dict[str | None, str]


TEI_NAMESPACE: Final = "http://www.tei-c.org/ns/1.0"
TEI: Final[NamespacesKWArgs] = {"namespaces": {None: TEI_NAMESPACE}}

# TODO a simple storage-related plugin makes more sense in light of the sublass.py
#      contained example


class TEIHeader(DocumentMixinBase):
    @classmethod
    def _init_config(cls, config: SimpleNamespace, kwargs: Dict[str, Any]):
        config.tei_header = SimpleNamespace(
            yelling=kwargs.pop("tei_header_yelling", False)
        )
        super()._init_config(config, kwargs)

    @property
    def tei_header(self):
        return TEIHeaderProperties(self)


class TEIHeaderProperties:
    def __init__(self, document):
        self.document = document

    @property
    def authors(self):
        return [
            x.full_text
            for x in self.document.css_select(
                "teiHeader fileDesc sourceDesc biblFull titleStmt author", **TEI
            )
        ]

    @property
    def title(self):
        result = self.document.css_select(
            "teiHeader fileDesc titleStmt title", **TEI
        ).first.full_text.strip()
        if self.document.config.tei_header.yelling:
            result = result.upper()
        return result
