# note that nothing is imported from the top-level `delb` module as it would
# trigger the loading of plugins, yet the plugins in this module hasn't been
# registered yet
from types import SimpleNamespace
from typing import Any, Dict

from _delb.plugins import plugin_manager, DocumentMixinHooks


# TODO a simple storage-related plugin makes more sense in light of the sublass.py
#      contained example


@plugin_manager.register_document_extension
class TEIHeader(DocumentMixinHooks):
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
                "teiHeader fileDesc sourceDesc biblFull titleStmt author"
            )
        ]

    @property
    def title(self):
        result = self.document.css_select(
            "teiHeader fileDesc titleStmt title"
        ).first.full_text.strip()
        if self.document.config.tei_header.yelling:
            result = result.upper()
        return result
