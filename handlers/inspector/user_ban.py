"""Забинить пользователя"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from filters.inspector import IsInspector
from keyboards.inspector import ban_user

router = Router()


@router.callback_query(F.data.startswith("ban_"), IsInspector())
async def show_inspectors(callback: CallbackQuery):
    """Подтверждение блокирования пользователя."""
    user_id = callback.data.split("_")[1]
    await callback.message.edit_reply_markup(reply_markup=ban_user(user_id))
