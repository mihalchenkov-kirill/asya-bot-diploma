from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник!')


@user_private_router.message(Command('menu'))
async def menu_command(message: types.Message):
    await message.answer('Вот меню:')


@user_private_router.message(Command('about'))
async def about_command(message: types.Message):
    await message.answer('(с) Я бот - Ася.')


@user_private_router.message(F.text)
async def magic_filter_text(message: types.Message):
    await message.answer('Магический фильтр - текст')


@user_private_router.message(F.photo)
async def magic_filter_photo(message: types.Message):
    await message.answer('Магический фильтр - фото')
