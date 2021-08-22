import pytest
from holodex.client import HolodexClient


@pytest.mark.asyncio
async def test_autocomplete():
    async with HolodexClient() as client:
        channel = await client.autocomplete("gura")
        assert channel.contents[0].text == "Gawr Gura Ch. hololive-EN"
