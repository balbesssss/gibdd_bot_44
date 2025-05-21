"""Список инспекторов"""

from aiogram import Router, F
from aiogram.types import Message
from database.models import User, UserRole
from filters.admin import IsAdmin
from filters.inspector import IsInspector

router = Router()


@router.message(F.text == "Показать инспекторов", IsAdmin())
async def show_inspectors(message: Message):
    """Отображает список инспекторов администратору."""
    inspectors = (
        User.select().join(UserRole).where(UserRole.role == IsInspector.role)
    )
    if not inspectors:
        await message.answer("Список инспекторов пуст.")
        return
    inspectors_list = "<b>Список инспекторов:</b>\n"
    for i, inspector in enumerate(inspectors, 1):
        full_name = (
            f"{inspector.first_name or ''} {inspector.last_name or ''}".strip()
        )
        if inspector.username:
            inspector_entry = (
                f'{i}. <a href="https://t.me/{inspector.username}">'
                f"{full_name}</a>"
            )
        else:
            inspector_entry = f"{i}. {full_name}"
        inspectors_list += inspector_entry + "\n"
    await message.answer(
        inspectors_list, parse_mode="HTML", disable_web_page_preview=True
    )


@router.message(F.text == "Показать администраторов", IsAdmin())
async def show_admins(message: Message):
    """Отображает список администраторов администратору."""
    admins = (
        User.select().join(UserRole).where(UserRole.role == IsAdmin.role)
    )

    if not admins:
        await message.answer('Список администраторов пуст')
        return

    admins_list = '<b>Список администраторов:</b>\n'
    for index, admin in enumerate(admins, 1):
        full_name = (
            f"{admin.first_name or ''} {admin.last_name or ''}".strip()
        )
        if admin.username:
            admin_entry = (
                f'{index}. <a href="https://t.me/{admin.username}">'
                f"{full_name}</a>"
            )
        else:
            admin_entry = f"{index}. {full_name}"
        admins_list += admin_entry + "\n"
    await message.answer(
        admins_list, parse_mode="HTML", disable_web_page_preview=True
    )