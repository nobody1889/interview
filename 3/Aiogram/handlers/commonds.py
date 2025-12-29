from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router(name="commonds")

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("wellcome to echo bot 🚀🚀🚀🚀🚀")

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("you just to need send a text to me and i will send it back to you")