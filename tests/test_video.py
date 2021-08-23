import pytest


@pytest.mark.asyncio
async def test_video_info(client):
    video = await client.video("fLAcgHX160k")
    assert video.title == "The Advent of Omegaα"
