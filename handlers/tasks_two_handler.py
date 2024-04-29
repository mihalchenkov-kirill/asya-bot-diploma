from aiogram import F, Router, types

from constants.inline_ready_buttons import STAGES
from kbds.inline import get_callback_buttons
from placeholders.pictures.tasks_two import tasks_two
from placeholders.texts import tasks_two_text

tasks_two_router = Router()


@tasks_two_router.callback_query(F.data == 'tasks_step_two')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_1,
        caption=tasks_two_text.tasks_two_1,
        reply_markup=get_callback_buttons(buttons={'Начнем!': 'tasks_step_two_next_2'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_2')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_2,
        caption=tasks_two_text.tasks_two_2,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_3'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_3')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_3,
        caption=tasks_two_text.tasks_two_3,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_4'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_4')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_4,
        caption=tasks_two_text.tasks_two_4,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_5'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_5')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_5,
        caption=tasks_two_text.tasks_two_5,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_6'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_6')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_6,
        caption=tasks_two_text.tasks_two_6,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_7'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_7')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_7,
        caption=tasks_two_text.tasks_two_7,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_8'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_8')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_8,
        caption=tasks_two_text.tasks_two_8,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_9'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_9')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_9,
        caption=tasks_two_text.tasks_two_9,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_10'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_10')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks_two.tasks_two_10,
        caption=tasks_two_text.tasks_two_10,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_two_next_11'}),
    )


@tasks_two_router.callback_query(F.data == 'tasks_step_two_next_11')
async def _(callback: types.CallbackQuery):
    (await callback.message.answer(text=tasks_two_text.tasks_two_12, reply_markup=STAGES),)
