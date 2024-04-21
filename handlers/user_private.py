from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart, or_f

from commons.get_clinic_address import get_clinic_address
from kbds.inline import get_callback_buttons
from kbds.reply import get_keyboard

user_private_router = Router()


@user_private_router.message(or_f(CommandStart(), F.text == 'Перезапустить бота'))
async def start_cmd(message: types.Message):
    await message.answer(
        'Привет, я виртуальный помощник!',
        reply_markup=get_keyboard(
            'Перезапустить бота',
            '🏥️Найти ближайший центр психологической помощи 🏥️️',
            'Подсказать',
            'Показать меню',
            'О боте',
            placeholder='Что вас интересует?',
            request_location=1,
            sizes=(1, 1, 3),
        ),
    )


@user_private_router.message(or_f(Command('menu'), F.text == 'Показать меню'))
async def menu_command(message: types.Message):
    await message.answer(
        'Вот меню:',
        reply_markup=get_callback_buttons(buttons={'Перезапустить бота': 'restart_bot', 'О боте': 'about_bot'}),
    )


@user_private_router.callback_query(F.data == 'about_bot')
async def about_command_callback(callback: types.CallbackQuery):
    await callback.message.edit_text('(с) Я бот - Ася.')


@user_private_router.message(or_f(Command('about'), F.text == 'О боте'))
async def about_command(message: types.Message):
    await message.answer('(с) Я бот - Ася.')


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.delete()
    await message.answer(get_clinic_address(message.location.latitude, message.location.longitude))


@user_private_router.message(F.text)
async def magic_filter_text(message: types.Message):
    await message.answer('Магический фильтр - текст')


@user_private_router.message(F.photo)
async def magic_filter_photo(message: types.Message):
    await message.answer('Магический фильтр - фото')
