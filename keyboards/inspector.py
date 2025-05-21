"""Клавиатуры для инспектора"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

USER_BAN = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="Подтвердить",
            callback_data='user_ban_confirm'
            ),
        InlineKeyboardButton(
            text="Отменить",
            callback_data='user_ban_cancel'
        ),
    ]])

MESSAGE_USER = InlineKeyboardMarkup(

    inline_keyboard=[[

        InlineKeyboardButton(text="Бан", callback_data='Ban'),

    ]])
