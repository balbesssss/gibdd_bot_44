"""Модуль обработки регистраций"""
from aiogram.types import Message, CallbackQuery
from bot.handlers.crud import create_user_profile

async def command_start_handler(message: Message) -> None:
    """Обработчик команды /start
    Выбор типа пользователя
    """
    tg_id = message.from_user.id
    username = message.from_user.username
    last_name = message.from_user.last_name
    first_name = message.from_user.first_name
    # telephone = message.user.
    # await create_user_profile()
    await message.answer("Добрый день. Через этого бота Вы можете отправить анонимное сообщение о пьяном водителе")
    await (f'{message}')
