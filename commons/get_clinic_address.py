import logging
import os
from urllib.parse import quote

import requests

from constants import response_codes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

session = requests.Session()


def get_clinic_address(latitude, longitude):
    place = 'Психолог'
    radius = '1500'
    api_url = 'https://catalog.api.2gis.com/3.0/items'
    params = {
        'q': place,
        'sort_point': f'{longitude},{latitude}',
        'radius': radius,
        'work_time': 'now',
        'key': os.getenv('MAP_TOKEN'),
    }
    try:
        response = session.get(api_url, params=params)
        logging.info(f'URL запроса: {response.url}')
        if response.status_code == response_codes.RESPONSE_CODE_OK:
            return parse_response(response.json())
        else:
            logging.error(f'Ошибка сервера: статус код {response.status_code}')
            return 'Ошибка при получении адресов'
    except requests.RequestException as e:
        logging.error(f'Ошибка сети: {e}')
        return 'Сетевая ошибка при выполнении запроса'


def parse_response(data):
    items = data.get('result', {}).get('items', [])
    if items:
        first_name = items[0].get('name', 'Название не найдено')
        first_address = items[0].get('address_name', 'Адрес не найден')
        route_link = f'https://www.google.com/maps/dir/?api=1&destination={quote(first_address)}'
        return f"<b>Ближайший адрес:\n{first_name}</b>\nМаршрут: <a href='{route_link}'>google maps</a>"
    else:
        return 'Адресов не найдено'
