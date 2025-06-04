"""Забинить пользователя"""

from datetime import datetime, timedelta
from asyncio import sleep
from aiogram import exceptions
from aiogram import Router, F
from aiogram.types import CallbackQuery
from filters import IsEmployee, IsAdmin
from keyboards.employee import user_ban_cobfirm_and_cancel_kb, user_ban_kb
from database.models import Message, User, UserRole

router = Router()


@router.callback_query(F.data.startswith("ban_"), IsEmployee())
async def show_inspectors(callback: CallbackQuery):
    """Подтверждение блокирования пользователя."""
    user_id = callback.data.split("_")[-1]
    await callback.message.edit_reply_markup(
        reply_markup=user_ban_cobfirm_and_cancel_kb(user_id)
    )


@router.callback_query(F.data.startswith("user_ban_confirm_"), IsEmployee())
async def blocking_user(callback: CallbackQuery):
    """Блокировка пользователя."""
    user_id = int(callback.data.split("_")[-1])
    user_to_block = User.get(User.tg_id == user_id)
    inspector = User.get(User.tg_id == callback.from_user.id)

    if user_to_block.is_ban:
        await callback.answer("Пользователь заблокирован.")
        return

    ban_duration = timedelta(days=30) if user_to_block.ban_counter > 0 else timedelta(days=1)
    ban_end_date = datetime.now() + ban_duration

    user_to_block.is_ban = True
    user_to_block.ban_counter += 1
    user_to_block.ban_end_date = ban_end_date
    user_to_block.save()

    try:
        await callback.bot.send_message(
            chat_id=user_to_block.tg_id,
            text=f"Вы получили бан до {ban_end_date.strftime('%d-%m-%Y %H:%M')}"
        )
    except exceptions.TelegramAPIError:
        print(f"Не удалось отправить сообщение пользователю {user_to_block.tg_id}")

    message_list = list(
        Message.select().where(Message.from_user == user_to_block)
    )

    for message in message_list:
        try:
            await callback.bot.delete_message(
                chat_id=message.to_user.tg_id,
                message_id=message.tg_message_id,
            )
        except exceptions.TelegramBadRequest:
            print(f"Сообщение {message.tg_message_id} не найдено")

    Message.update(is_delete=True).where(
        Message.tg_message_id.in_([m.tg_message_id for m in message_list])
    ).execute()

    admins = User.select().join(UserRole).where(UserRole.role == IsAdmin.role)

    inspector = User.get(User.tg_id == callback.from_user.id)
    for admin in admins:
        try:
            if callback.message.reply_to_message:
                await callback.bot.forward_message(
                    chat_id=admin.tg_id,
                    from_chat_id=callback.message.chat.id,
                    message_id=callback.message.reply_to_message.message_id
                )
            
            await callback.bot.send_message(
                chat_id=admin.tg_id,
                text=(
                    f"Пользователь {user_to_block.full_name} "
                    f"заблокирован сотрудником {inspector.full_name}\n"
                    f"Срок бана до: {ban_end_date.strftime('%d-%m-%Y %H:%M')}\n"
                    f"Это {user_to_block.ban_counter} бан пользователя"
                )
            )
            await sleep(0.5)
        except exceptions.TelegramAPIError:
            print(f"Не удалось отправить сообщение администратору {admin.tg_id}")

    await callback.answer("Пользователь успешно заблокирован.")

@router.callback_query(F.data.startswith("user_ban_cancel_"), IsEmployee())
async def unblocking_user(callback: CallbackQuery):
    """Отмена блокировки пользователя."""
    user_id = callback.data.split("_")[-1]
    await callback.message.edit_reply_markup(reply_markup=user_ban_kb(user_id))

@router.message(F.from_user.id.in_(User.select().where(User.is_ban == True)))
async def handle_banned_user_message(message: Message):
    user = User.get(User.tg_id == message.from_user.id)
    if user.ban_end_date and datetime.now() < user.ban_end_date:
        await message.answer(
            f"Вы не можете писать до срока окончания бана, "
            f"напишите снова после {user.ban_end_date.strftime('%d-%m-%Y %H:%M')}"
        )
    else:
        user.is_ban = False
        user.save()