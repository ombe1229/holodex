# holodex

> Holodex api wrapper

## Example

```py
import asyncio
from holodex.client import HolodexClient


async def main():
    async with HolodexClient() as client:
        gura = await client.channel_info("UCoSrY_IQQVpmIRZ9Xf-y93g")
        print(gura.name)
        print(gura.clip_count)
        print(gura.subscriber_count)


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
