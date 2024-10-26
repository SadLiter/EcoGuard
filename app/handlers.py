from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.keyboards import keyboard


router = Router()

@router.message(CommandStart())
async def register(message: Message):
    await message.answer('Я - EcoGuard, твой личный AI помощник.\nПришлите мне файл формата Word или PDF', reply_markup=keyboard)


@router.message(F.document)
async def handle_document(message: types.Message):
    document = message.document
    file_name = document.file_name

    # Проверяем расширение файла
    if file_name.endswith('.pdf') or file_name.endswith('.docx') or file_name.endswith('.doc'):
        # Получаем файл
        file_id = document.file_id
        file = await message.bot.get_file(file_id)
        # Сохраняем файл на диск
        await message.bot.download_file(file.file_path, f"./{file_name}")

        await message.answer(f"Файл '{file_name}' успешно загружен.")
        # Здесь можно добавить логику обработки файла
    else:
        await message.answer("Пожалуйста, отправьте файл в формате PDF или Word (DOCX).")

@router.message(F.text)
async def handle_chat_with_ai(message: types.Message):
    if message.text == "Чат с AI":
        await message.answer("Вы начали чат с AI. Какой у вас вопрос?")
        # Здесь вы можете добавить логику общения с AI

@router.message(lambda message: not message.document)
async def invalid_file(message: types.Message):
    await message.answer("Пожалуйста, отправьте файл, а не текст.")
