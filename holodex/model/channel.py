from typing import Any, List, Literal, Optional


class ChannelInfo:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def name(self) -> str:
        return self._response["name"]

    @property
    def english_name(self) -> Optional[str]:
        return self._response["english_name"]

    @property
    def description(self) -> str:
        return self._response["description"]

    @property
    def photo(self) -> Optional[str]:
        return self._response["photo"]

    @property
    def thumbnail(self) -> str:
        return self._response["thumbnail"]

    @property
    def banner(self) -> Optional[str]:
        return self._response["banner"]

    @property
    def org(self) -> Optional[str]:
        return self._response["org"]

    @property
    def suborg(self) -> Optional[str]:
        return self._response["suborg"]

    @property
    def lang(self) -> Optional[str]:
        return self._response["lang"]

    @property
    def published_at(self) -> str:
        return self._response["published_at"]

    @property
    def view_count(self) -> Optional[str]:
        return self._response["view_count"]

    @property
    def video_count(self) -> Optional[str]:
        return self._response["video_count"]

    @property
    def subscriber_count(self) -> Optional[str]:
        return self._response["subscriber_count"]

    @property
    def comments_crawled_at(self) -> str:
        return self._response["comments_crawled_at"]

    @property
    def updated_at(self) -> str:
        return self._response["updated_at"]

    @property
    def yt_uploads_id(self) -> str:
        return self._response["yt_uploads_id"]

    @property
    def crawled_at(self) -> str:
        return self._response["crawled_at"]

    @property
    def type(self) -> Literal["vtuber", "subber"]:
        return self._response["type"]

    @property
    def clip_count(self) -> Optional[int]:
        return self._response["clip_count"]

    @property
    def twitter(self) -> Optional[str]:
        return self._response["twitter"]

    @property
    def inactive(self) -> bool:
        return self._response["inactive"]

    @property
    def created_at(self) -> str:
        return self._response["created_at"]

    @property
    def top_topics(self) -> List[str]:
        return self._response["top_topics"]
