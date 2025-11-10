from typing import Any

from _delb.plugins import plugin_manager
from _delb.xpath import EvaluationContext


@plugin_manager.register_xpath_function("is-lower")
def is_lower(_: EvaluationContext, value: Any) -> str:
    if not isinstance(value, str):
        raise TypeError
    return value.lower()
