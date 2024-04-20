import os
from urllib.parse import quote

import requests

from constans import response_codes


def get_clinic_address(latitude, longitude):
    place = 'Психолог'
    radius = '1500'
    url = f"https://catalog.api.2gis.com/3.0/items?q={place}&sort_point={longitude},{latitude}&radius={radius}&key={os.getenv('MAP_TOKEN')}"
    response = requests.get(url)
    print(url)
    if response.status_code == response_codes.RESPONSE_CODE_OK:
        data = response.json()
        items = data.get('result', {}).get('items', [])
        if items:
            first_name = items[0].get('name', 'Название не найдено')
            first_address = items[0].get('address_name', 'Адрес не найден')
            route_link = f'https://www.google.com/maps/dir/?api=1&destination={quote(first_address)}'
            return f"<b>Ближайший адрес:\n{first_name}</b>\nМаршрут: <a href='{route_link}'>google maps</a>"
        else:
            return 'Адресов не найдено'
    else:
        return 'Ошибка при получении адресов'
