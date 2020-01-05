# note that nothing is imported from the top-level delb module as it would trigger
# the loading of plugins, yet the plugins in this module hasn't been registered yet

from delb.plugins import plugin_manager
from delb.plugins.contrib.core_loaders import text_loader


@plugin_manager.register_loader(before=text_loader)
def remote_loader(source, config):
    if isinstance(source, str) and source.startswith("remote://"):
        return text_loader(f'<document url="{source}"/>', config)
    return None, {}
