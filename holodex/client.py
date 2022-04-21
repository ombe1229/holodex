from typing import Any, Optional

from aiohttp.client import ClientSession
from typing_extensions import Literal

from holodex.http import HolodexHttpClient
from holodex.model.autocomplete import AutoComplete
from holodex.model.channel import Channel
from holodex.model.channel_video import ChannelVideo
from holodex.model.channels import Channels
from holodex.model.live import Live
from holodex.model.search_comment import SearchComment
from holodex.model.search_video import SearchVideo
from holodex.model.video import Video


class HolodexClient(HolodexHttpClient):
    def __init__(
        self, key: Optional[str] = None, session: Optional[ClientSession] = None
    ) -> None:
        super().__init__(key, session)

    def __get_params(
        self, keys: dict[str, Any], exclude: Optional[list[str]] = None
    ) -> dict[str, Any]:
        keys.pop("self")
        if exclude:
            for key in exclude:
                keys.pop(key)
        return {k: v for k, v in keys.items() if v is not None}

    async def channel(self, channel_id: str) -> Channel:
        return Channel(await self.get_channel(channel_id))

    async def channels(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        type: Optional[Literal["vtuber"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive", "Nijisanji", "Independents"]
        ] = None,
        sort: Optional[str] = None
    ) -> Channels:
        params = self.__get_params(locals())
        return Channels(await self.get_channels(**params))

    async def autocomplete(self, keyword: str) -> AutoComplete:
        return AutoComplete(await self.get_autocomplete(keyword))

    async def live_streams(
        self,
        *,
        channel_id: Optional[str] = None,
        id: Optional[str] = None,
        include: Optional[list[str]] = None,
        lang: Optional[Literal["all", "en", "ja"]] = None,
        limit: Optional[int] = None,
        max_upcoming_hours: Optional[int] = None,
        mentioned_channel_id: Optional[str] = None,
        offset: Optional[int] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive", "Nijisanji", "Independents"]
        ] = None,
        paginated: Optional[str] = None,
        sort: Optional[str] = None,
        status: Optional[str] = None,
        topic: Optional[str] = None,
        type: Optional[str] = None
    ) -> Live:
        params = self.__get_params(locals())
        return Live(await self.get_live_streams(params))

    async def video(self, video_id: str) -> Video:
        params = {"c": 1, "lang": "all"}
        return Video(await self.get_video(video_id, params))

    async def videos_from_channel(
        self,
        channel_id: str,
        type: Literal["clips", "videos", "collabs"],
        include: Optional[list[str]] = None,
        lang: Optional[Literal["all", "en", "ja"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        paginated: Optional[str] = None,
    ) -> ChannelVideo:
        params = self.__get_params(locals(), ["channel_id", "type"])
        return ChannelVideo(
            await self.get_videos_from_channel(channel_id, type, params)
        )

    async def search_video(
        self,
        offset: int,
        limit: int,
        sort: Literal["oldest", "newest"] = "newest",
        lang: Optional[Literal["all", "en", "ja"]] = None,
        target: Optional[Literal["clip", "stream"]] = None,
        conditions: Optional[list[dict[Literal["text"], str]]] = None,
        topic: Optional[list[str]] = None,
        vch: Optional[list[str]] = None,
        org: Optional[list[str]] = None,
    ) -> SearchVideo:
        params = self.__get_params(locals(), ["offset", "limit", "sort"])
        return SearchVideo(await self.get_search_video(params))

    async def search_comment(
        self,
        comment: str,
        offset: int,
        limit: int,
        sort: Literal["oldest", "newest"] = "newest",
        lang: Optional[list[str]] = None,
        target: Optional[list[Literal["clip", "stream"]]] = None,
        topic: Optional[list[str]] = None,
        vch: Optional[list[str]] = None,
        org: Optional[list[str]] = None,
        paginated: Optional[str] = None,
    ) -> SearchComment:
        params = self.__get_params(locals(), ["comment", "offset", "limit", "sort"])
        return SearchComment(await self.get_search_comment(params))
