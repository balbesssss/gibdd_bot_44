"""Клавиатуры для инспектора"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

USER_BAN = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Подтвердить", callback_data='Confirm'),
        InlineKeyboardButton(text="Отменить", callback_data='Cancel'),
    ]])
