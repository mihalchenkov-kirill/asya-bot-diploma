from aiogram import F, Router, types

from constans.inline_ready_buttons import YES_OR_NO
from kbds.inline import get_callback_buttons
from placeholders.texts import show_info_text

MYSTERY_YES = get_callback_buttons(buttons={'Давай!': 'mystery_yes', 'Нет!': 'back_to_menu'})
AFTER_MYSTERY_YES = get_callback_buttons(buttons={'Давай!': 'after_mystery_yes', 'Нет!': 'back_to_menu'})
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
    await callback.message.edit_text(show_info_text.mystery_1, reply_markup=YES_OR_NO)


@show_info_handler_router.callback_query(F.data == 'answer_yes')
async def step_one(callback: types.CallbackQuery):
    await callback.message.edit_text(show_info_text.mystery_2, reply_markup=MYSTERY_YES)


@show_info_handler_router.callback_query(F.data == 'mystery_yes')
async def step_two(callback: types.CallbackQuery):
    await callback.message.edit_text(show_info_text.mystery, reply_markup=MYSTERY_ANSWERS)


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_instinct')
async def answer_instinct(callback: types.CallbackQuery):
    await callback.message.answer(show_info_text.mystery_3)


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_wolf')
async def answer_wolf(callback: types.CallbackQuery):
    await callback.message.answer(show_info_text.mystery_4)


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_sad')
async def answer_sad(callback: types.CallbackQuery):
    await callback.message.answer(show_info_text.mystery_5)


@show_info_handler_router.callback_query(F.data == 'mystery_bad_choice_emotion')
async def answer_emotion(callback: types.CallbackQuery):
    await callback.message.answer(show_info_text.mystery_6)


@show_info_handler_router.callback_query(F.data == 'mystery_right_choice')
async def answer_right(callback: types.CallbackQuery):
    await callback.message.answer(show_info_text.mystery_7, reply_markup=AFTER_MYSTERY_YES)


@show_info_handler_router.callback_query(F.data == 'after_mystery_yes')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_8,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'mystery_next_1'}),
    )


@show_info_handler_router.callback_query(F.data == 'mystery_next_1')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_9,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'mystery_next_2'}),
    )


@show_info_handler_router.callback_query(F.data == 'mystery_next_2')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_10,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'mystery_next_3'}),
    )


@show_info_handler_router.callback_query(F.data == 'mystery_next_3')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_11, reply_markup=get_callback_buttons(buttons={'Далее!': 'mystery_next_4'})
    )


@show_info_handler_router.callback_query(F.data == 'mystery_next_4')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_12, reply_markup=get_callback_buttons(buttons={'Далее!': 'mystery_next_5'})
    )


@show_info_handler_router.callback_query(F.data == 'mystery_next_5')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_13, reply_markup=get_callback_buttons(buttons={'Далее!': 'mystery_next_6'})
    )


@show_info_handler_router.callback_query(F.data == 'mystery_next_6')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_14,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'zzz'}),
    )


@show_info_handler_router.callback_query(F.data == 'zzz')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        show_info_text.mystery_15,
    )
