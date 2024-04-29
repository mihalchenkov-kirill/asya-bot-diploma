from aiogram import F, Router, types

from constants.inline_ready_buttons import RETURN_TO_MENU
from kbds.inline import get_callback_buttons, get_mixed_buttons
from placeholders.pictures.extra_help import extra_help
from placeholders.texts import extra_help_text

extra_help_router = Router()


@extra_help_router.callback_query(F.data == 'extra_help')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=extra_help.extra_help1,
        caption=extra_help_text.extra_1,
        reply_markup=get_callback_buttons(buttons={'Далее': 'extra_next_1'}),
    )


@extra_help_router.callback_query(F.data == 'extra_next_1')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=extra_help.extra_help2,
        caption=extra_help_text.extra_2,
        reply_markup=get_mixed_buttons(
            buttons={'Далее': 'extra_next_2', 'МЧС России онлайн': 'https://psi.mchs.gov.ru/'}, sizes=(1, 1)
        ),
    )


@extra_help_router.callback_query(F.data == 'extra_next_2')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=extra_help.extra_help4,
        caption=extra_help_text.extra_3,
        reply_markup=get_mixed_buttons(
            buttons={
                'Далее': 'extra_next_3',
                'Кризисная психологическая служба для детей и подростков': 'https://szgmu.ru/',
            },
            sizes=(1, 1),
        ),
    )


@extra_help_router.callback_query(F.data == 'extra_next_3')
async def _(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=extra_help.extra_help3,
        caption=extra_help_text.extra_4,
        reply_markup=get_mixed_buttons(
            buttons={'Далее': 'extra_next_4', 'Социальный проект «Без паники»': 'https://bez-paniki.online/'},
            sizes=(1, 1),
        ),
    )


@extra_help_router.callback_query(F.data == 'extra_next_4')
async def _(callback: types.CallbackQuery):
    await callback.message.answer(text=extra_help_text.extra_5, reply_markup=RETURN_TO_MENU)
