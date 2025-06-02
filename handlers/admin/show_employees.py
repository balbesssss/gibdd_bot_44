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
async def go_to_page_handler(callback: CallbackQuery):
    """Обрабатывает переход по страницам инспекторов"""

    args = callback.data.split("_")
    page = int(args[-1])
    role_id = int(args[-2])
    keyboard = get_kb_by_show_employees(
        role=role_id,
        page=page
    )

    await callback.message.edit_text(
        f"<b>Список инспекторов:</b> (страница {page})",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


@router.message(F.text == "Показать администраторов", IsAdmin())
async def show_admins(message: Message):
    """Отображает список администраторов администратору."""
    keyboard = get_kb_by_show_employees(
        role=IsAdmin.role,
        page=1
    )

    await message.answer(
        "<b>Список администраторов:</b> (страница 1)",
        parse_mode="HTML",
        reply_markup=keyboard
    )

