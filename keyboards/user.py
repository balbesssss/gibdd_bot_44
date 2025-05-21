"""Клавиатуры для Администратора"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

MESUSER = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Бан", callback_data='Ban'),
    ]])
