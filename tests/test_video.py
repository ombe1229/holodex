import pytest
from holodex.client import HolodexClient


@pytest.mark.asyncio
async def test_video_info():
    async with HolodexClient() as client:
        video = await client.video("fLAcgHX160k")
        assert video.title == "The Advent of Omegaα"
