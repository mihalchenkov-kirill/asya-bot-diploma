import requests

from constans import response_codes


def get_full_address(latitude, longitude):
    url = f'https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json'
    response = requests.get(url)
    if response.status_code == response_codes.RESPONSE_CODE_OK:
        data = response.json()
        address = data.get('display_name', 'Адрес не найден')
        return address
    else:
        return 'Ошибка при получении адреса'
