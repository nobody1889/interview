from aiogram import Router, types

router = Router(name="echo")

@router.message()
async def echo(message: types.Message):
    await message.answer(message.text)