from aiogram import F, Router, types
from aiogram.filters import CommandStart

from constans.inline_ready_buttons import MAIN_MENU
from placeholders import text

menu_handler_router = Router()


@menu_handler_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text.welcome_text.format(user_name=message.from_user.first_name), reply_markup=MAIN_MENU)


@menu_handler_router.callback_query(F.data == 'back_to_menu')
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text('Главное меню', reply_markup=MAIN_MENU)
