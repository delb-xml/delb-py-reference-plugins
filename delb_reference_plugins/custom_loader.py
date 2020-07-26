# note that nothing is imported from the top-level `delb` module as it would
# trigger the loading of plugins, yet the plugins in this module hasn't been
# registered yet

from _delb.plugins import plugin_manager
from _delb.plugins.core_loaders import text_loader
from _delb.typing import LoaderResult


@plugin_manager.register_loader(before=text_loader)
def remote_loader(source, config) -> LoaderResult:
    if isinstance(source, str) and source.startswith("remote://"):
        config.source_url = source
        return text_loader(f'<document url="{source}"/>', config)
    return "The input value is not an URL with the remote scheme."
