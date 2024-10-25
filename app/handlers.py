from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message()
async def return_message(message: Message):
    await message.answer(message.text)