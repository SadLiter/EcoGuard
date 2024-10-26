from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Создаем кнопку "Чат с AI"
keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Чат с AI")]
],
resize_keyboard=True)