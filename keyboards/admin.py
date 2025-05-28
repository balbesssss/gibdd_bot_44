"""Клавиатуры для Администратора"""

from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from database.models import User, Admin


ADMIN_KEYBOARD = [
    [
        KeyboardButton(text="Добавить инспектора"),
        KeyboardButton(text="Показать инспекторов"),
    ],
    [
        KeyboardButton(text="Добавить администратора"),
        KeyboardButton(text="Показать администраторов"),
    ],
]


def get_keyboard_by_user(user: User):
    """Кнопки для клавиатуры администратора"""

    admin: Admin = Admin.get_or_none(user=user)
    keyboard = ADMIN_KEYBOARD + [[
        (
            KeyboardButton(text="Не получать сообщения очевидцев")
            if admin and admin.is_notify
            else KeyboardButton(text="Получать соощения очевидцев")
        )
    ]]
    return keyboard


def get_kb_by_user(user: User):
    """Клавиатура администратора"""
    keyboard = get_keyboard_by_user(user)
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
