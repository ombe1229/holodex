from aiohttp import ClientSession
from typing import Any, Literal, Optional
from types import TracebackType


class HolodexHttpClient:
    BASE_URL = "https://holodex.net/api/v2"

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self.session = session

    async def close(self) -> None:
        if self.session:
            await self.session.close()

    async def __aenter__(self) -> "HolodexHttpClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def request(
        self, method: Literal["GET", "POST"], endpoint: str, **kwargs: Any
    ) -> Any:
        if not self.session:
            self.session = ClientSession()

        async with self.session.request(
            method, self.BASE_URL + endpoint, **kwargs
        ) as r:
            return await r.json()

    async def get_channel(self, channel_id: str) -> Any:
        return await self.request("GET", f"/channels/{channel_id}")

    async def get_autocomplete(self, q: str) -> Any:
        return await self.request("GET", f"/search/autocomplete", params={"q": q})

    async def get_live_streams(self, params: dict[str, Any]) -> Any:
        return await self.request("GET", f"/live", params=params)

    async def get_video(self, video_id: str, params: dict[str, Any]) -> Any:
        return await self.request("GET", f"/videos/{video_id}", params=params)

    async def get_videos_from_channel(
        self,
        channel_id: str,
        type: Literal["clips", "videos", "collabs"],
        params: dict[str, Any],
    ) -> Any:
        return await self.request(
            "GET", f"/channels/{channel_id}/{type}", params=params
        )

    async def get_search_video(self, params: dict[str, Any]) -> Any:
        return await self.request("POST", "/search/videoSearch", params=params)
