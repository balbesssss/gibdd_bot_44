"""Клавиатуры для Администратора"""


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


MESSAGE_USER = InlineKeyboardMarkup(

    inline_keyboard=[[

        InlineKeyboardButton(text="Бан", callback_data='Ban'),

    ]])
