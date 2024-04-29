import logging
import os
from typing import Any

import httpx
from aiogram import F, Router, flags, types
from aiogram.fsm.context import FSMContext
from dotenv import find_dotenv, load_dotenv

from constants import response_codes
from fsm.states import Generate

chat_router = Router()

load_dotenv(find_dotenv())


async def chat_asya(messages_history, prompt) -> tuple[Any, Any] | None:
    try:
        url = 'https://apisbost.top/v1/chat/completions'
        headers = {
            'Authorization': f"Bearer {os.getenv('AI_TOKEN')}",
            'Content-Type': 'application/json',
        }
        data = {'model': 'gpt-3.5-turbo', 'messages': messages_history + [{'role': 'user', 'content': prompt}]}

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, headers=headers, json=data)

        if response.status_code == response_codes.RESPONSE_CODE_OK:
            result = response.json()
            return result['choices'][0]['message']['content'], result['usage']['total_tokens']
        else:
            logging.error(f'Request failed with status code {response.status_code}: {response.text}')
            return None
    except Exception:
        logging.exception('An exception occurred during the chat API request')
        return None


@chat_router.callback_query(F.data == 'chat_with_bot')
async def input_text_prompt(callback: types.CallbackQuery, state: FSMContext):
    initial_context = [
        {"role": "user", "content": "Привет, ты виртуальный психотерапевт по имени Ася. Поздоровайся со мной и начнем сеанс."},
    ]
    await state.set_state(Generate.text_prompt)
    await state.update_data(messages_history=initial_context)
    await callback.message.answer('Введите ваш запрос:')


@chat_router.message(Generate.text_prompt)
@flags.chat_action('typing')
async def generate_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    messages_history = data.get('messages_history', [])
    prompt = message.text
    response = await chat_asya(messages_history, prompt)
    if response is None:
        return await message.answer('Ошибка при обработке запроса')

    response_text, _ = response
    await message.answer(response_text, disable_web_page_preview=True)

    messages_history.append({'role': 'user', 'content': prompt})
    messages_history.append({'role': 'assistant', 'content': response_text})
    await state.update_data(messages_history=messages_history)
