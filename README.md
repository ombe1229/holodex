# holodex

[![PyPI version](https://badge.fury.io/py/holodex.svg)](https://badge.fury.io/py/holodex) [![PyPI downloads](https://img.shields.io/pypi/dm/holodex.svg)](https://pypi.python.org/pypi/holodex) [![CodeFactor](https://www.codefactor.io/repository/github/ombe1229/holodex/badge)](https://www.codefactor.io/repository/github/ombe1229/holodex) [![Build Status](https://app.travis-ci.com/ombe1229/holodex.svg?branch=master)](https://app.travis-ci.com/ombe1229/holodex)

> Holodex api wrapper

## Example

```py
import asyncio
from holodex.client import HolodexClient


async def main():
    async with HolodexClient() as client:
        channel = await client.channel_info("UCoSrY_IQQVpmIRZ9Xf-y93g")
        print(channel.name)
        print(channel.clip_count)
        print(channel.subscriber_count)


asyncio.run(main())


# Gawr Gura Ch. hololive-EN
# 6943
# 3240000
```

## Installation

```
python -m pip install holodex
```

## Todo

- [x] Support `/live` endpoint
- [x] Make easy to get channel id
- [ ] Support `/videos` endpoint
- [ ] Travis
