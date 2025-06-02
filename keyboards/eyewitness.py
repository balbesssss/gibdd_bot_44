"""Клавиатуры для очевидцев"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

KB = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text="Отправить геолокацию",
                request_location=True,
                callback_data="request_location",
            )
        ]
    ],
)
