from typing import Optional
from aiohttp.client import ClientSession

from holodex.http import HolodexHttpClient
from holodex.model.channel_info import ChannelInfo


class HolodexClient(HolodexHttpClient):
    """
    Holodex client
    """

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        super().__init__(session)

    async def channel_info(self, channel_id: str) -> ChannelInfo:
        """
        ## channel_info
        Get channel info by channel id

        ### Parameters
         - `channel_id` (str): channel id

        ### Returns
         - Class `ChannelInfo`

        """
        return ChannelInfo(await self.get_channel(channel_id))
