import logging
import os
from typing import Any

import httpx
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI

from constans import response_codes

load_dotenv(find_dotenv())


aclient = AsyncOpenAI(api_key=os.getenv('AI_TOKEN'))


async def generate_text(prompt) -> tuple[Any, Any] | None:
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {os.getenv('AI_TOKEN')}",
            "Content-Type": "application/json",
        }
        data = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)

        if response.status_code == response_codes.RESPONSE_CODE_OK:
            result = response.json()
            return result["choices"][0]["message"]["content"], result["usage"]["total_tokens"]
        else:
            logging.error(f"Request failed with status code {response.status_code}")
            return None
    except Exception as e:
        logging.error(e)
        return None
