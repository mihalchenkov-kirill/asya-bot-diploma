from aiogram import F, Router, types

from constants.inline_ready_buttons import STAGES
from kbds.inline import get_callback_buttons
from placeholders.pictures.tasks import tasks
from placeholders.texts import tasks_text

tasks_router = Router()


@tasks_router.callback_query(F.data == 'tasks')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks1,
        caption=tasks_text.tasks_1,
        reply_markup=STAGES,
    )


@tasks_router.callback_query(F.data == 'tasks_step_one')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks2,
        caption=tasks_text.tasks_2,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_one_next_2'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_2')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks3,
        caption=tasks_text.tasks_3,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_one_next_3'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_3')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks4,
        caption=tasks_text.tasks_4,
        reply_markup=get_callback_buttons(buttons={'Я готов!': 'tasks_step_one_next_4'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_4')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks5,
        caption=tasks_text.tasks_5,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_one_next_5'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_5')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks6,
        caption=tasks_text.tasks_6,
        reply_markup=get_callback_buttons(buttons={'Пропускаем пока что мысли.': 'tasks_step_one_next_6'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_6')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks7,
        caption=tasks_text.tasks_7,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_one_next_7'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_7')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks123,
        caption=tasks_text.tasks_8,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_one_next_8'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_8')
async def _(callback: types.CallbackQuery):
    await callback.message.answer(
        photo=tasks.tasks9,
        caption=tasks_text.tasks_9,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_one_next_9'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_9')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=tasks.tasks321,
        caption=tasks_text.tasks_10,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_one_next_10'}),
    )


@tasks_router.callback_query(F.data == 'tasks_step_one_next_10')
async def _(callback: types.CallbackQuery):
    await callback.message.answer(
        text=tasks_text.tasks_11,
        reply_markup=STAGES,
    )
