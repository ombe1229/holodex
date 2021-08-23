from typing import Any, Literal, Optional


class Channel:
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
        return self._response.get("english_name")

    @property
    def description(self) -> Optional[str]:
        return self._response.get("description")

    @property
    def photo(self) -> Optional[str]:
        return self._response["photo"]

    @property
    def thumbnail(self) -> Optional[str]:
        return self._response.get("thumbnail")

    @property
    def banner(self) -> Optional[str]:
        return self._response.get("banner")

    @property
    def org(self) -> Optional[str]:
        return self._response.get("org")

    @property
    def suborg(self) -> Optional[str]:
        return self._response.get("suborg")

    @property
    def lang(self) -> Optional[str]:
        return self._response.get("lang")

    @property
    def published_at(self) -> Optional[str]:
        return self._response.get("published_at")

    @property
    def view_count(self) -> Optional[str]:
        return self._response.get("view_count")

    @property
    def video_count(self) -> Optional[str]:
        return self._response.get("video_count")

    @property
    def subscriber_count(self) -> Optional[str]:
        return self._response.get("subscriber_count")

    @property
    def comments_crawled_at(self) -> Optional[str]:
        return self._response.get("comments_crawled_at")

    @property
    def updated_at(self) -> Optional[str]:
        return self._response.get("updated_at")

    @property
    def yt_uploads_id(self) -> Optional[str]:
        return self._response.get("yt_uploads_id")

    @property
    def crawled_at(self) -> Optional[str]:
        return self._response.get("crawled_at")

    @property
    def type(self) -> Optional[Literal["vtuber", "subber"]]:
        return self._response.get("type")

    @property
    def clip_count(self) -> Optional[int]:
        return self._response.get("clip_count")

    @property
    def twitter(self) -> Optional[str]:
        return self._response.get("twitter")

    @property
    def inactive(self) -> Optional[bool]:
        return self._response.get("inactive")

    @property
    def created_at(self) -> Optional[str]:
        return self._response.get("created_at")

    @property
    def top_topics(self) -> Optional[list[str]]:
        return self._response.get("top_topics")
