from typing import Any, Dict, Literal
from holodex.model.channel import Channel


class LiveInfo:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def title(self) -> str:
        return self._response["title"]

    @property
    def type(self) -> str:
        return self._response["type"]

    @property
    def topic_id(self) -> str:
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
    def live_tl_count(self) -> Dict[str, int]:
        return self._response["live_tl_count"]

    @property
    def start_scheduled(self) -> str:
        return self._response["start_scheduled"]

    @property
    def start_actual(self) -> str:
        return self._response["start_actual"]

    @property
    def live_viewers(self) -> int:
        return self._response["live_viewers"]

    @property
    def channel(self) -> Channel:
        return Channel(self._response["channel"])


class Live:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def contents(self) -> list[LiveInfo]:
        return [LiveInfo(content) for content in self._response]
