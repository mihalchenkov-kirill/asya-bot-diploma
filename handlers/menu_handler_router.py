from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile

from constans.inline_ready_buttons import MAIN_MENU, RETURN_TO_MENU
from placeholders.texts import main_text

menu_handler_router = Router()

menu = FSInputFile('placeholders/pictures/commons/main_welcome.jpg')


@menu_handler_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer_photo(
        photo=menu,
        caption=main_text.welcome_text.format(user_name=message.from_user.first_name),
        reply_markup=MAIN_MENU
    )
    # await message.answer('11', reply_markup=MAIN_MENU)
    # await message.answer(main_text.welcome_text.format(user_name=message.from_user.first_name), reply_markup=MAIN_MENU)


@menu_handler_router.callback_query(F.data == 'about_bot')
async def about(callback: types.CallbackQuery):
    await callback.message.edit_text('(с) Я бот - Ася.', reply_markup=RETURN_TO_MENU)


@menu_handler_router.callback_query(F.data == 'back_to_menu')
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text('Главное меню', reply_markup=MAIN_MENU)
