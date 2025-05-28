"""Пересылка локации от пользователя инспекторам"""

from aiogram import Router, F
from aiogram.types import Message
from filters.user import IsUser
from handlers.eyewitness.common import send_message_to_employees

# pylint: disable=E1101

router = Router()


@router.message(F.location, IsUser())
async def get_location_from_user(message: Message):
    """Обработчик локации от пользователя"""
    await send_message_to_employees(message)