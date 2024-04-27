from aiogram import F, Router, types, flags
from aiogram.fsm.context import FSMContext

from commons import utils
from fsm.states import Generate

chat_router = Router()
ACCESS = False


@chat_router.callback_query(F.data == 'chat_with_bot')
async def _(callback: types.CallbackQuery):
    if ACCESS:
        await callback.message.answer('Test')
    else:
        await callback.answer('Временно недоступно!', show_alert=True)


# @chat_router.callback_query(F.data == "chat_with_bot")
# async def input_text_prompt(callback: types.CallbackQuery, state: FSMContext):
#     await state.set_state(Generate.text_prompt)
#     # await callback.message.edit_text('Генеретим')
#     await callback.message.answer('Генеретим')
#
#
# @chat_router.message(Generate.text_prompt)
# @flags.chat_action("typing")
# async def generate_text(message: types.Message, state: FSMContext):
#     prompt = message.text
#     mesg = await message.answer('Генеретим')
#     res = await utils.generate_text(prompt)
#     if not res:
#         return await mesg.edit_text('Ошибка')
#     await mesg.edit_text(res[0], disable_web_page_preview=True)
