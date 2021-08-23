from typing import Any, Literal, Optional
from holodex.model.channel import Channel


class ChannelVideoInfo:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def title(self) -> str:
        return self._response["title"]

    @property
    def type(self) -> Literal["stream", "clip"]:
        return self._response["type"]

    @property
    def topic_id(self) -> Optional[str]:
        return self._response["topic_id"]

    @property
    def published_at(self) -> str:
        return self._response["published_at"]

    @property
    def available_at(self) -> str:
        return self._response["available_at"]

    @property
    def duration(self) -> int:
        return self._response["duration"]

    @property
    def status(self) -> Literal["new", "upcoming", "live", "past", "missing"]:
        return self._response["status"]

    @property
    def channel(self) -> Channel:
        return Channel(self._response["channel"])


class ChannelVideo:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def contents(self) -> list[ChannelVideoInfo]:
        return [ChannelVideoInfo(content) for content in self._response]
