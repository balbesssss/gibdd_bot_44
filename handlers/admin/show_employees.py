"""Список инспекторов"""
from aiogram import Router, F
from aiogram.types import Message
from database.models import User, UserRole, Role

router = Router()

@router.message(F.text == "Показать инспекторов")
async def show_inspectors(message: Message):
    inspector_role = Role.get(name="Инспектор")
    inspectors = User.select().join(UserRole).where(UserRole.role == inspector_role)
    
    if not inspectors:
        await message.answer("Список инспекторов пуст.")
        return
    
    inspectors_list = "<b>Список инспекторов:</b>\n"
    for i, inspector in enumerate(inspectors, 1):
        full_name = f"{inspector.first_name or ''} {inspector.last_name or ''}".strip()
        
        if inspector.username:
            inspector_entry = f'{i}. <a href="https://t.me/{inspector.username}">{full_name}</a>'
        else:
            inspector_entry = f"{i}. {full_name}"
        
        inspectors_list += inspector_entry + "\n"
    
    await message.answer(inspectors_list, parse_mode="HTML")