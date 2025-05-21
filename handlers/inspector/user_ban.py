"""Забинить пользователя"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from filters.inspector import IsInspector
from keyboards.inspector import USER_BAN

router = Router()


@router.callback_query(F.data == "Ban", IsInspector())
async def show_inspectors(callback: CallbackQuery):
    """Подтверждение блокирования пользователя."""
    await callback.message.edit_reply_markup(reply_markup=USER_BAN)
