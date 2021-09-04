from typing import Any, Literal
from holodex.model.channel import Channel


class SearchVideo:
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
    def available_at(self) -> str:
        return self._response["available_at"]

    @property
    def duration(self) -> int:
        return self._response["duration"]

    @property
    def status(self) -> Literal["new", "upcoming", "live", "past", "missing"]:
        return self._response["status"]

    @property
    def start_scheduled(self) -> str:
        return self._response["start_scheduled"]

    @property
    def start_actual(self) -> str:
        return self._response["start_actual"]

    @property
    def end_actual(self) -> str:
        return self._response["end_actual"]

    @property
    def live_viewers(self) -> int:
        return self._response["live_viewers"]

    @property
    def description(self) -> str:
        return self._response["description"]

    @property
    def songcount(self) -> int:
        return self._response["songcount"]

    @property
    def channel_id(self) -> str:
        return self._response["channel_id"]

    @property
    def channel(self) -> Channel:
        return Channel(self._response["channel"])


class Condition:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def text(self) -> str:
        return self._response["text"]
        