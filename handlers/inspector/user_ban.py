"""Забинить пользователя"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from filters.inspector import IsInspector
from keyboards.inspector import user_ban_cobfirm_and_cancel_kb
from database.models import Message, User

router = Router()


@router.callback_query(F.data.startswith("ban_"), IsInspector())
async def show_inspectors(callback: CallbackQuery):
    """Подтверждение блокирования пользователя."""
    user_id = callback.data.split("_")[1]
    await callback.message.edit_reply_markup(
        reply_markup=user_ban_cobfirm_and_cancel_kb(user_id)
    )


@router.callback_query(F.data.startswith("user_ban_confirm_"), IsInspector())
async def blocking_user(callback: CallbackQuery):
    """Отмена блокирования пользователя."""
    user_id = callback.data.split("_")[3]
    user = User.get_or_none(User.tg_id == user_id)
    message_list = list(
        Message.select().where(Message.user == user)
    )
    for message in message_list:
        await callback.bot.delete_message(
            chat_id=message.user.tg_id,
            message_id=message.tg_message_id
        )
        message.delete_instance()
    user.is_ban = True
    user.save()


@router.callback_query(F.data.startswith("user_ban_cancel_"), IsInspector())
async def Unblocking_user(callback: CallbackQuery):
    """Разблокировка пользователя."""
    await callback.message.edit_reply_markup(
        reply_markup=False
    )
