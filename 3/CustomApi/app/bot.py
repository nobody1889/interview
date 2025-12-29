from .utils.telegram_api import TelegtamApi
from handlers.core import core
import asyncio
class Bot:
    def __init__(self):
        self.api = TelegtamApi()
        self.offset = None

    async def run(self):
        while True:
            updates = await self.api.get_updates(self.offset)
            await core(self.api, updates)

if __name__ == "__main__":
    bot = Bot()
    asyncio.run(bot.run())