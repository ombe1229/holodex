import pytest
from holodex.client import HolodexClient


@pytest.mark.asyncio
async def test_channel_info():
    async with HolodexClient() as client:
        channel = await client.channel_info("UCCzUftO8KOVkV4wQG1vkUvg")
        assert channel.created_at == "2021-04-23T07:21:00.045Z"
