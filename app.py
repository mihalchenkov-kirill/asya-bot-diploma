import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.utils.chat_action import ChatActionMiddleware
from dotenv import find_dotenv, load_dotenv

from commons.bot_cmds_list import private
from constants.allowed_updates import ALLOWED_UPDATES
from handlers.chat_handler import chat_router
from handlers.extra_help_handler import extra_help_router
from handlers.find_clinic_handler import find_clinic_router
from handlers.menu_handler_router import menu_handler_router
from handlers.show_info_handler import show_info_handler_router
from handlers.tasks_handler import tasks_router
from handlers.tasks_three_handler import tasks_three_router
from handlers.tasks_two_handler import tasks_two_router

load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)

dp.message.middleware(ChatActionMiddleware())

dp.include_router(menu_handler_router)
dp.include_router(show_info_handler_router)
dp.include_router(tasks_router)
dp.include_router(tasks_two_router)
dp.include_router(tasks_three_router)
dp.include_router(chat_router)
dp.include_router(find_clinic_router)
dp.include_router(extra_help_router)

# ruff: noqa
# need for locust
# @dp.message(F.text)
# async def handle_message(message: types.Message):
#     chat_id = message.chat.id
#     await message.answer(f"Received your message! Chat ID: {chat_id}")
# ruff: noqa


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
