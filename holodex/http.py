from aiohttp import ClientSession
from typing import Any, Literal, Optional
from types import TracebackType


class HolodexHttpClient:
    BASE_URL = "https://holodex.net/api/v2"

    def __init__(
        self, key: Optional[str] = None, session: Optional[ClientSession] = None
    ) -> None:
        self.session = session
        self.key = key

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

    @property
    def headers(self) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        if self.key:
            headers["X-APIKEY"] = self.key
        return headers

    async def request(
        self,
        method: Literal["GET", "POST"],
        endpoint: str,
        **kwargs: Any,
    ) -> Any:
        if not self.session:
            self.session = ClientSession()

        async with self.session.request(
            method,
            self.BASE_URL + endpoint,
            headers=self.headers,
            **kwargs,
        ) as r:
            return await r.json()

    async def get_channel(self, channel_id: str) -> Any:
        return await self.request("GET", f"/channels/{channel_id}")

    async def get_channels(self, **params: Any) -> Any:
        return await self.request(
            "GET", f"/channels", params={"limit": 100, "offset": 100, **params}
        )

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
