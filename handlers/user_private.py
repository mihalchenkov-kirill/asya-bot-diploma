from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart, or_f

from common.get_sber_address import get_sber_address
from kbds import reply

user_private_router = Router()


@user_private_router.message(or_f(CommandStart(), F.text == 'Перезапустить бота'))
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник!', reply_markup=reply.start_kb)


@user_private_router.message(or_f(Command('menu'), F.text == 'Показать меню'))
async def menu_command(message: types.Message):
    await message.answer('Вот меню:', reply_markup=reply.del_kbd)


@user_private_router.message(or_f(Command('about'), F.text == 'О боте'))
async def about_command(message: types.Message):
    await message.answer('(с) Я бот - Ася.')


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(get_sber_address(message.location.latitude, message.location.longitude))


@user_private_router.message(F.text)
async def magic_filter_text(message: types.Message):
    await message.answer('Магический фильтр - текст')


@user_private_router.message(F.photo)
async def magic_filter_photo(message: types.Message):
    await message.answer('Магический фильтр - фото')
