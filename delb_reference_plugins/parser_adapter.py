import re
from typing import Iterator

from _delb.parser import Event, EventType, ParserOptions, TagEventData
from _delb.plugins import XMLEventParserInterface
from _delb.typing import BinaryReader
from _delb.xpath.tokenizer import alternatives, named_group


token_iterator = re.compile(
    alternatives(
        named_group("tagstart", r"<[a-z]+>"),
        named_group("tagend", r"</[a-z]+>"),
        named_group("text", "[a-zA-Z]+"),
    )
).finditer


class ParserAdapterDemo(XMLEventParserInterface):
    name = "dumbo"

    def __init__(self, options: ParserOptions, base_url: str | None, encoding: str):
        pass

    def parse(self, data: BinaryReader | str) -> Iterator[Event]:
        assert isinstance(data, str)

        for match_object in token_iterator(data):
            match match_object.lastgroup:
                case "tagstart":
                    yield (
                        EventType.TagStart,
                        TagEventData(
                            namespace="",
                            local_name=match_object.group()[1:-1],
                            attributes={},
                        )
                    )
                case "tagend":
                    yield EventType.TagEnd, None
                case "text":
                    yield EventType.Text, match_object.group().upper()
                case _:
                    raise NotImplementedError
