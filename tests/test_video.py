import pytest
from holodex.client import HolodexClient


@pytest.mark.asyncio
async def test_video_info():
    async with HolodexClient() as client:
        channel = await client.video("7Lt-b2Eq99Y")
        assert channel.clips[0].id == "GbywVgGs9cU"
