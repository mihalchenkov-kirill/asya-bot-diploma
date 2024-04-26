from aiogram import F, Router, types

chat_router = Router()
ACCESS = False


@chat_router.callback_query(F.data == 'chat_with_bot')
async def _(callback: types.CallbackQuery):
    if ACCESS:
        await callback.message.answer('Test')
    else:
        await callback.answer('Временно недоступно!', show_alert=True)
