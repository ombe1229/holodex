from typing import Any, Literal, Optional
from holodex.model.channel import Channel


class SearchVideoInfo:
    def __init__(self, content: Any) -> None:
        self._content = content

    @property
    def id(self) -> str:
        return self._content["id"]

    @property
    def title(self) -> str:
        return self._content["title"]

    @property
    def type(self) -> Literal["stream", "clip"]:
        return self._content["type"]

    @property
    def published_at(self) -> str:
        return self._content["published_at"]

    @property
    def available_at(self) -> str:
        return self._content["available_at"]

    @property
    def duration(self) -> int:
        return self._content["duration"]

    @property
    def status(self) -> Literal["new", "upcoming", "live", "past", "missing"]:
        return self._content["status"]

    @property
    def start_scheduled(self) -> Optional[str]:
        return self._content["start_scheduled"]

    @property
    def start_actual(self) -> Optional[str]:
        return self._content["start_actual"]

    @property
    def end_actual(self) -> Optional[str]:
        return self._content["end_actual"]

    @property
    def live_viewers(self) -> Optional[int]:
        return self._content["live_viewers"]

    @property
    def description(self) -> Optional[str]:
        return self._content["description"]

    @property
    def songcount(self) -> Optional[int]:
        return self._content.get("songcount")

    @property
    def channel_id(self) -> str:
        return self._content["channel_id"]

    @property
    def channel(self) -> Channel:
        return Channel(self._content["channel"])


class SearchVideo:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def items(self) -> list[SearchVideoInfo]:
        return [SearchVideoInfo(item) for item in self._response]
