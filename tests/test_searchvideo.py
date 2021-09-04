import pytest


@pytest.mark.asyncio
async def test_autocomplete(client):
    search = await client.search_video(offset=0, limit=5, lang=["en", "ja"], target=["stream", "clip"], topic=["singing"], org=["Nijisanji", "Hololive"])
    assert search.contents[0].id == "7kbxZyarbH8"
