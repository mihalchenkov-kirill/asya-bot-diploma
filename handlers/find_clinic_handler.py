from aiogram import F, Router, types

from commons.get_clinic_address import get_clinic_address
from constans.inline_ready_buttons import MAIN_MENU
from kbds.reply import del_keyboard, get_keyboard

find_clinic_router = Router()


@find_clinic_router.callback_query(F.data == 'find_clinic')
async def about_command_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        'Вам необходимо найти ближайшую клинку?',
        reply_markup=get_keyboard(
            'Нет, не нужно.',
            'Да, давайте найдем.',
            placeholder='Нажмите кнопку',
            request_location=1,
            sizes=(1, 1),
        ),
    )


@find_clinic_router.message(F.location)
async def get_location(message: types.Message):
    await message.delete()
    await message.answer(
        get_clinic_address(message.location.latitude, message.location.longitude), reply_markup=del_keyboard()
    )


@find_clinic_router.message(F.text == 'Нет, не нужно.')
async def _(message: types.Message):
    await message.answer('Главное меню', reply_markup=MAIN_MENU)
