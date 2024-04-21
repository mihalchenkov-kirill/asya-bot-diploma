from aiogram import F, Router, types

from constans.inline_ready_buttons import YES_OR_NO
from kbds.inline import get_callback_buttons
from placeholders import text

MYSTERY_YES = get_callback_buttons(buttons={'Давай!': 'mystery_yes', 'Нет!': 'back_to_menu'})
MYSTERY_ANSWERS = get_callback_buttons(
    buttons={
        'Инстинкт': 'mystery_bad_choice_instinct',
        'Волк': 'mystery_bad_choice_wolf',
        'Мысли': 'mystery_right_choice',
        'Плохое настроение': 'mystery_bad_choice_sad',
        'Эмоции': 'mystery_bad_choice_emotion',
    },
    sizes=(1, 1, 1, 1, 1),
)

show_info_handler_router = Router()


@show_info_handler_router.callback_query(F.data == 'show_info')
async def send_info(callback: types.CallbackQuery):
    await callback.message.edit_text('Моя цель помочь. Соглы?', reply_markup=YES_OR_NO)


@show_info_handler_router.callback_query(F.data == 'answer_yes')
async def step_one(callback: types.CallbackQuery):
    await callback.message.edit_text('Загадка...! Соглы на загадку?', reply_markup=MYSTERY_YES)


@show_info_handler_router.callback_query(F.data == 'mystery_yes')
async def step_two(callback: types.CallbackQuery):
    await callback.message.edit_text(text.mystery, reply_markup=MYSTERY_ANSWERS)


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_instinct')
async def answer_instinct(callback: types.CallbackQuery):
    await callback.message.answer('Инстинкт? Нет!')


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_wolf')
async def answer_wolf(callback: types.CallbackQuery):
    await callback.message.answer('Волк? Нет!')


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_sad')
async def answer_sad(callback: types.CallbackQuery):
    await callback.message.answer('Плохое настроение? Нет!')


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_emotion')
async def answer_emotion(callback: types.CallbackQuery):
    await callback.message.answer('Эмоции? Нет!')
