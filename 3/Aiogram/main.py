import asyncio
from aiogram import Bot, Dispatcher

from config import bot_token
from handlers.echo import router as echo_router
from handlers.commonds import router as commond_router


async def main():
    bot = Bot(token=bot_token)
    dp = Dispatcher()

    dp.include_router(commond_router)
    dp.include_router(echo_router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
