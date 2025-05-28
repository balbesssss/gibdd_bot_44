"""Пересылка сообщения от пользователя инспекторам"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.user import IsUser
from handlers.eyewitness.common import send_message_to_employees

# pylint: disable=E1101

router = Router()


@router.message(F.text, ~F.text.startswith("/"), IsUser())
async def get_message_from_user(message: Message):
    """Обработчик сообщения от пользователя"""

    await send_message_to_employees(message)

    # Создаем Inline клавиатуру с кнопкой "Отправить геолокацию"
    builder = InlineKeyboardBuilder()
    builder.button(text="Отправить геолокацию", callback_data="request_location")
    
    await message.answer(
        "Если нужно отправить геолокацию, нажмите кнопку ниже:",
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "request_location")
async def handle_location_request(callback: CallbackQuery):
    """Обработчик кнопки 'Отправить геолокацию'"""
    await callback.answer()
    await callback.message.answer(
        "Пожалуйста, отправьте вашу геолокацию через меню вложения (скрепка -> Геолокация)."
        )
