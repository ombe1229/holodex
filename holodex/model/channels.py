from typing import Any, Union
from typing_extensions import Literal


class LiteChannel:
    _response: Any

    def __init__(self, response: Any) -> None:
        self._response: Any = response

    def __repr__(self):
        return f'LiteChannel("{self.id}", "{self.name}")'

    @property
    def id(self) -> str:
        return self._response.get("id")

    @property
    def name(self) -> str:
        return self._response.get("name")

    @property
    def english_name(self) -> str:
        return self._response.get("english_name")

    @property
    def type(self) -> Union[Literal["vtuber"], str]:
        return self._response.get("type")

    @property
    def org(self):
        return self._response.get("org")

    @property
    def suborg(self):
        return self._response.get("suborg")

    @property
    def group(self) -> str:
        return self._response.get("group")

    @property
    def photo(self) -> str:
        return self._response.get("photo")

    @property
    def twitter(self) -> str:
        return self._response.get("twitter")

    @property
    def video_count(self) -> int:
        return int(self._response.get("video_count"))

    @property
    def subscriber_count(self) -> int:
        return int(self._response.get("subscriber_count"))

    @property
    def clip_count(self) -> int:
        return self._response.get("clip_count")

    @property
    def top_topics(self) -> list[str]:
        return self._response.get("top_topics")


class Channels:
    _response: list[Any]

    def __init__(self, response: list[Any]) -> None:
        if type(response) == list:
            self._response = [LiteChannel(channel) for channel in response]
        else:
            self._response = response

    def __repr__(self):
        return f"Channels({len(self)})"

    def __getitem__(self, index: Union[slice, int]) -> Union[LiteChannel, Any]:
        return self._response.__getitem__(index)

    def __len__(self):
        return len(self._response)
