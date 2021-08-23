from holodex.model.channel_video import ChannelVideo
from holodex.model.video import Video
from holodex.model.live import Live
from holodex.model.autocomplete import AutoComplete
from typing import Any, Literal, Optional
from aiohttp.client import ClientSession

from holodex.http import HolodexHttpClient
from holodex.model.channel import Channel


class HolodexClient(HolodexHttpClient):
    def __init__(self, session: Optional[ClientSession] = None) -> None:
        super().__init__(session)

    def __get_params(
        self, keys: dict[str, Any], exclude: Optional[list[str]] = None
    ) -> dict[str, Any]:
        keys.pop("self")
        for key in exclude:
            keys.pop(key)
        return {k: v for k, v in keys.items() if v is not None}

    async def channel(self, channel_id: str) -> Channel:
        return Channel(await self.get_channel(channel_id))

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
