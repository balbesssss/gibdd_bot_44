"""Забинить пользователя"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from filters.inspector import IsInspector
from keyboards.inspector import user_ban_cobfirm_and_cancel_kb

router = Router()


@router.callback_query(F.data.startswith("ban_"), IsInspector())
async def show_inspectors(callback: CallbackQuery):
    """Подтверждение блокирования пользователя."""
    user_id = callback.data.split("_")[1]
    await callback.message.edit_reply_markup(
        reply_markup=user_ban_cobfirm_and_cancel_kb(user_id)
    )
