import pytest


@pytest.mark.asyncio
async def test_autocomplete(client):
    channel = await client.autocomplete("gawr gura ch")
    assert channel.contents[0].text == "Gawr Gura Ch. hololive-EN"
