from typing import Any

from holodex.model.search_info import SearchInfo


class SearchVideoInfo(SearchInfo):
    def __init__(self, content: Any) -> None:
        super().__init__(content)


class SearchVideo:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def items(self) -> list[SearchVideoInfo]:
        return [SearchVideoInfo(item) for item in self._response]
