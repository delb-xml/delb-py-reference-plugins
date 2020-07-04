# note that nothing is imported from the top-level delb module as it would trigger
# the loading of plugins, yet the plugins in this module hasn't been registered yet

from _delb.plugins import plugin_manager
from _delb.utils import first


@plugin_manager.register_document_extension
class HeaderProperties:

    @property
    def authors(self):
        result = []
        for name_node in self.css_select("header authors person name"):
            forename = first(name_node.css_select("forename")).full_text.strip()
            surname = first(name_node.css_select("surname")).full_text.strip()
            result.append(f"{forename} {surname}")
        return result

    @property
    def title(self):
        return first(self.css_select("header title mainTitle")).full_text.strip()
