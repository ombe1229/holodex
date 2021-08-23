import pytest

from holodex.client import HolodexClient


@pytest.fixture()
async def client():
    client = HolodexClient()
    yield client
    if client.session:
        await client.session.close()
