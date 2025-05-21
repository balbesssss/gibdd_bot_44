"""Клавиатуры для Администратора"""
from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
    )

KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить инспектора"),
            KeyboardButton(text="Показать инспекторов"),
        ],
        [
            KeyboardButton(text="Добавить администратора"),
            KeyboardButton(text="Показать администраторов"),
        ],
    ],
    resize_keyboard=True,
)
