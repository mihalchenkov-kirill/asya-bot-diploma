import os
from urllib.parse import quote

import requests

from constans import response_codes


def get_sber_address(latitude, longitude):
    place = 'Психиатрическая помощь'
    url = f"https://catalog.api.2gis.com/3.0/items?q={place}&sort_point={longitude},{latitude}&key={os.getenv('MAP_TOKEN')}"
    response = requests.get(url)
    print(url)
    if response.status_code == response_codes.RESPONSE_CODE_OK:
        data = response.json()
        items = data.get('result', {}).get('items', [])
        if items:
            first_name = items[0].get('name', 'Название не найдено')
            first_address = items[0].get('address_name', 'Адрес не найден')
            route_link = f'https://www.google.com/maps/dir/?api=1&destination={quote(first_address)}'
            return f"<b>{first_name}</b>\nПостроить маршрут: <a href='{route_link}'>google maps</a>"
        else:
            return 'Адресов не найдено'
    else:
        return 'Ошибка при получении адресов'
