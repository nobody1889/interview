from aiogram import Router, types
from aiogram.filters import CommandStart
router = Router(name="commonds")

@router.command("start")
async def start_command(message: types.Message):
    await message.answer("wellcome to echo bot 🚀🚀🚀🚀🚀")