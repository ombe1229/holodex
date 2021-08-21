from holodex.model.live import Live
from holodex.model.autocomplete import AutoComplete
from typing import Literal, Optional
from aiohttp.client import ClientSession

from holodex.http import HolodexHttpClient
from holodex.model.channel_info import ChannelInfo


class HolodexClient(HolodexHttpClient):
    def __init__(self, session: Optional[ClientSession] = None) -> None:
        super().__init__(session)

    async def channel_info(self, channel_id: str) -> ChannelInfo:
        return ChannelInfo(await self.channels(channel_id))

    async def autocomplete(self, keyword: str) -> AutoComplete:
        return AutoComplete(await self.search_autocomplete(keyword))

    async def live_streams(
        self,
        org: Optional[
            Literal["All Vtubers", "Hololive", "Nijisanji", "Independents"]
        ] = "All Vtubers",
    ) -> Live:
        return Live(await self.live(org))
