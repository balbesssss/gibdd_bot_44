"""Список инспекторов"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database.models import User, UserRole
from filters.admin import IsAdmin
from filters.inspector import IsInspector
from keyboards.admin import get_kb_by_show_employees

router = Router()


@router.message(F.text == "Показать инспекторов", IsAdmin())
async def show_inspectors(message: Message):
    """Отображает список инспекторов администратору."""
    keyboard = get_kb_by_show_employees(role=IsInspector.role, page=1)

    await message.answer(
        "<b>Список инспекторов:</b> (страница 1)",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


@router.callback_query(F.data.startswith("users_page_"), IsAdmin())
async def handle_inspector_page(callback: CallbackQuery):
    """Обрабатывает переход по страницам инспекторов"""
    page = int(callback.data.split("_")[-1])

    keyboard = get_kb_by_show_employees(role=IsInspector.role, page=page)

    await callback.message.edit_text(
        f"<b>Список инспекторов:</b> (страница {page})",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


@router.message(F.text == "Показать администраторов", IsAdmin())
async def show_admins(message: Message):
    """Отображает список администраторов администратору."""
    admins = User.select().join(UserRole).where(UserRole.role == IsAdmin.role)

    if not admins:
        await message.answer("Список администраторов пуст")
        return

    admins_list = "<b>Список администраторов:</b>\n"
    for index, admin in enumerate(admins, 1):
        full_name = f"{admin.first_name or ''} {admin.last_name or ''}".strip()
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
