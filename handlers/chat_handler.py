import logging
import os
from typing import Any

import httpx
from aiogram import F, Router, flags, types
from aiogram.fsm.context import FSMContext
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI

from constans import response_codes
from fsm.states import Generate

chat_router = Router()


load_dotenv(find_dotenv())


aclient = AsyncOpenAI(api_key=os.getenv('AI_TOKEN'))


async def chat_asya(prompt) -> tuple[Any, Any] | None:
    try:
        # url = "https://api.openai.com/v1/chat/completions"
        url = 'https://apisbost.top/v1/chat/completions'
        headers = {
            'Authorization': f"Bearer {os.getenv('AI_TOKEN')}",
            'Content-Type': 'application/json',
        }
        data = {'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': prompt}]}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)

        if response.status_code == response_codes.RESPONSE_CODE_OK:
            result = response.json()
            return result['choices'][0]['message']['content'], result['usage']['total_tokens']
        else:
            logging.error(f'Request failed with status code {response.status_code}')
            return None
    except Exception as e:
        logging.error(e)
        return None


@chat_router.callback_query(F.data == 'chat_with_bot')
async def input_text_prompt(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Generate.text_prompt)
    # await callback.message.edit_text('Генеретим')
    await callback.message.answer('Генеретим')


@chat_router.message(Generate.text_prompt)
@flags.chat_action('typing')
async def generate_text(message: types.Message, state: FSMContext):
    prompt = message.text
    mesg = await message.answer('Генеретим')
    res = await chat_asya(prompt)
    if not res:
        return await mesg.edit_text('Ошибка')
    await mesg.edit_text(res[0], disable_web_page_preview=True)
