"""Модуль обработки команд"""
from aiogram.filters import CommandStart
from aiogram import Dispatcher, F
import bot.handlers.register as reg
import bot.state.state as stat
from api.RequestsUrl import AddressService
import bot.handlers.user_student as stu
import bot.handlers.user_teacher as tea
import bot.filters.cheak as cheak
from aiogram.filters import Command
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from datetime import datetime, timedelta

def function(dp: Dispatcher):
    """Регистрация команд"""
    dp.message.register(reg.command_start_handler, CommandStart())
