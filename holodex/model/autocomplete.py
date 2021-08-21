from typing import Any


class AutoCompleteInfo:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def type(self) -> str:
        return self._response["type"]

    @property
    def value(self) -> str:
        return self._response["value"]

    @property
    def text(self) -> str:
        return self._response["text"]


class AutoComplete:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def contents(self) -> list[AutoCompleteInfo]:
        return [AutoCompleteInfo(content) for content in self._response]
