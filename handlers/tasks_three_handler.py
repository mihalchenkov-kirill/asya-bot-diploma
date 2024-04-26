from aiogram import F, Router, types

from constans.inline_ready_buttons import MAIN_MENU
from kbds.inline import get_callback_buttons
from placeholders.pictures.tasks_three import tasks_three
from placeholders.texts import tasks_three_text

tasks_three_router = Router()


@tasks_three_router.callback_query(F.data == 'tasks_step_three')
async def _(callback: types.CallbackQuery):
    await callback.message.answer(
        text=tasks_three_text.tasks_three_1,
        reply_markup=get_callback_buttons(buttons={'Начнем!': 'tasks_step_three_next_2'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_2')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_2,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_3'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_3')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_3,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_4'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_4')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_4,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_5'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_5')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_5,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_6'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_6')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_6,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_7'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_7')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_7,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_8'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_8')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_8,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_9'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_9')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_9,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_10'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_10')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_10,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_11'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_11')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_11,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_12'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_12')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_12,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_13'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_13')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_13,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_14'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_14')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_14,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_15'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_15')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_15,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_16'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_16')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_16,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_17'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_17')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_17,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_18'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_18')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_18,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_19'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_19')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_19,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_20'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_20')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_20,
        reply_markup=get_callback_buttons(buttons={'Далее!': 'tasks_step_three_next_21'}),
    )


@tasks_three_router.callback_query(F.data == 'tasks_step_three_next_21')
async def _(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=tasks_three_text.tasks_three_21,
        reply_markup=MAIN_MENU,
    )
