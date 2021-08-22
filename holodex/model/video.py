from typing import Any, Literal


class ClipChannel:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def name(self) -> str:
        return self._response["name"]

    @property
    def photo(self) -> str:
        return self._response["photo"]


class ReferChannel:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def org(self) -> Literal["All Vtubers", "Hololive", "Nijisanji", "Independents"]:
        return self._response["org"]

    @property
    def name(self) -> str:
        return self._response["name"]

    @property
    def photo(self) -> str:
        return self._response["photo"]

    @property
    def english_name(self) -> str:
        return self._response["english_name"]


class RecommandationChannel:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def name(self) -> str:
        return self._response["name"]

    @property
    def type(self) -> Literal["vtuber", "subber"]:
        return self._response["type"]

    @property
    def photo(self) -> str:
        return self._response["photo"]


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
    def org(self) -> Literal["All Vtubers", "Hololive", "Nijisanji", "Independents"]:
        return self._response["org"]

    @property
    def type(self) -> Literal["vtuber", "subber"]:
        return self._response["type"]

    @property
    def photo(self) -> str:
        return self._response["photo"]

    @property
    def english_name(self) -> str:
        return self._response["english_name"]

    @property
    def view_count(self) -> str:
        return self._response["view_count"]

    @property
    def video_count(self) -> str:
        return self._response["video_count"]

    @property
    def subscriber_count(self) -> str:
        return self._response["subscriber_count"]

    @property
    def clip_count(self) -> int:
        return self._response["clip_count"]


class Clip:
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
    def channel(self) -> ClipChannel:
        return ClipChannel(self._response["channel"])


class Refer:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def type(self) -> Literal["stream", "clip"]:
        return self._response["type"]

    @property
    def title(self) -> str:
        return self._response["title"]

    @property
    def status(self) -> Literal["new", "upcoming", "live", "past", "missing"]:
        return self._response["status"]

    @property
    def channel(self) -> ReferChannel:
        return ReferChannel(self._response["channel"])

    @property
    def duration(self) -> int:
        return self._response["duration"]

    @property
    def available_at(self) -> str:
        return self._response["available_at"]


class Comment:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def comment_key(self) -> str:
        return self._response["comment_key"]

    @property
    def message(self) -> str:
        return self._response["message"]


class Recommendation:
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
    def channel(self) -> RecommandationChannel:
        return RecommandationChannel(self._response["channel"])


class VideoInfo:
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
    def start_scheduled(self) -> str:
        return self._response["start_scheduled"]

    @property
    def start_actual(self) -> str:
        return self._response["start_actual"]

    @property
    def end_actual(self) -> str:
        return self._response["end_actual"]

    @property
    def description(self) -> str:
        return self._response["description"]

    @property
    def clips(self) -> list[Clip]:
        return [Clip(clip) for clip in self._response["clips"]]

    @property
    def refers(self) -> list[Refer]:
        return [Refer(refer) for refer in self._response["refers"]]

    @property
    def channel(self) -> Channel:
        return Channel(self._response["channel"])

    @property
    def comments(self) -> list[Comment]:
        return [Comment(comment) for comment in self._response["comments"]]

    @property
    def recommendations(self) -> list[Recommendation]:
        return [
            Recommendation(recommendation)
            for recommendation in self._response["recommendations"]
        ]
