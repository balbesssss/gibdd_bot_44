"""Клавиатуры для Администратора"""

from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardButton, InlineKeyboardMarkup
    )

USER_BAN = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Подтвердить", callback_data='Confirm'),
        InlineKeyboardButton(text="Отменить", callback_data='Cancel'),
    ]])


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
