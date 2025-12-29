from aiogram import dispatcher, Bot, executor, types
from handlers.echo import router as echo_router
from handlers.commonds import router as commond_router
from config import bot_token
import asyncio

bot = Bot(token=bot_token)
dp = dispatcher.Dispatcher(bot)

dp.include_router(echo_router)
dp.include_router(commond_router)

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()
    

if __name__ == '__main__':
    asyncio.run(main())
