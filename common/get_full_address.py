import requests


def get_full_address(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        address = data.get('display_name', 'Адрес не найден')
        return address
    else:
        return 'Ошибка при получении адреса'
