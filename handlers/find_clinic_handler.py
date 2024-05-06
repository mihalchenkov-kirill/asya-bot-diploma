from aiogram import F, Router, types

from commons.get_clinic_address import get_clinic_address
from constants.inline_ready_buttons import MAIN_MENU, RETURN_TO_MENU
from kbds.reply import get_keyboard

find_clinic_router = Router()


@find_clinic_router.callback_query(F.data == 'find_clinic')
async def handle_find_clinic_request(callback: types.CallbackQuery):
    try:
        await callback.message.answer(
            'Вам необходимо найти ближайшую клинику?',
            reply_markup=get_keyboard(
                'Нет, не нужно.',
                'Да, давайте найдем.',
                placeholder='Нажмите кнопку',
                request_location=True,
                sizes=(1, 1),
            ),
        )
    except Exception:
        await callback.message.answer('Произошла ошибка. Пожалуйста, попробуйте позже.')


@find_clinic_router.message(F.location)
async def process_location(message: types.Message):
    try:
        await message.delete()
        address = get_clinic_address(message.location.latitude, message.location.longitude)
        await message.answer(address, reply_markup=RETURN_TO_MENU)
    except Exception:
        await message.answer('Не удалось получить адрес клиники. Пожалуйста, попробуйте еще раз.')


@find_clinic_router.message(F.text == 'Нет, не нужно.')
async def handle_negative_response(message: types.Message):
    await message.answer('Главное меню', reply_markup=MAIN_MENU)
