from .utils.telegram_api import TelegtamApi
from .handlers.core import core
import asyncio

class Bot:
    def __init__(self):
        self.api = TelegtamApi()
        self.offset = None

    async def run(self):
        while True:
            updates, self.offset = await self.api.get_updates(self.offset)
            await core(self.api, updates)
