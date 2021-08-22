from holodex.model.video import VideoInfo
from holodex.model.live import Live
from holodex.model.autocomplete import AutoComplete
from typing import Any, Literal, Optional
from aiohttp.client import ClientSession

from holodex.http import HolodexHttpClient
from holodex.model.channel import ChannelInfo


class HolodexClient(HolodexHttpClient):
    def __init__(self, session: Optional[ClientSession] = None) -> None:
        super().__init__(session)

    def __get_params(self, locals: dict[str, Any]):
        locals.pop("self")
        return {k: v for k, v in locals.items() if v is not None}

    async def channel(self, channel_id: str) -> ChannelInfo:
        return ChannelInfo(await self.get_channels(channel_id))

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
        return Live(await self.get_live(params))

    async def video(self, video_id: str) -> VideoInfo:
        params = {"c": 1, "lang": "all"}
        return VideoInfo(await self.get_video(video_id, params))
