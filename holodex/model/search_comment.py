from typing import Any

from holodex.model.search_info import SearchInfo


class Comment:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def comment_key(self) -> str:
        return self._response["comment_key"]

    @property
    def video_id(self) -> str:
        return self._response["video_id"]

    @property
    def message(self) -> str:
        return self._response["message"]


class SearchCommentInfo(SearchInfo):
    def __init__(self, content: Any) -> None:
        super().__init__(content)

    @property
    def comments(self) -> list[Comment]:
        return [Comment(comment) for comment in self._content["comments"]]


class SearchComment:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def items(self) -> list[SearchCommentInfo]:
        return [SearchCommentInfo(item) for item in self._response["items"]]
