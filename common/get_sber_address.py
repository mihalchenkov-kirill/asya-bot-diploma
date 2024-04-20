import os

import requests
from urllib.parse import quote


def get_sber_address(latitude, longitude):
    place = 'Психиатрическая помощь'
    url = f"https://catalog.api.2gis.com/3.0/items?q={place}&sort_point={longitude},{latitude}&key={os.getenv('MAP_TOKEN')}"
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        data = response.json()
        items = data.get('result', {}).get('items', [])
        if items:
            first_address = items[0].get('address_name', 'Адрес не найден')
            route_link = f"https://www.google.com/maps/dir/?api=1&destination={quote(first_address)}"
            return f"{first_address}\nПостроить маршрут: {route_link}"
        else:
            return 'Адресов не найдено'
    else:
        return 'Ошибка при получении адресов'
