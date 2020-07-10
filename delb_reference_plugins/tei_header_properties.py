# note that nothing is imported from the top-level delb module as it would trigger
# the loading of plugins, yet the plugins in this module hasn't been registered yet

from _delb.plugins import plugin_manager, DocumentExtensionHooks
from _delb.utils import first


@plugin_manager.register_document_extension
class TEIHeader(DocumentExtensionHooks):
    def _init_config(self, config_args):
        super()._init_config(config_args)
        self.tei_header = TEIHeaderProperties(self)


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
        return first(
            self.document.css_select("teiHeader fileDesc titleStmt title")
        ).full_text.strip()
