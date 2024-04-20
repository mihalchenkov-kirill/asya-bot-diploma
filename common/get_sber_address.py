import requests


def get_sber_address(latitude, longitude):
    key = "f837a207-d62f-4130-a1f7-1f913d111199"
    place = 'Психиатор'
    url = f"https://catalog.api.2gis.com/3.0/items?q={place}&sort_point={longitude},{latitude}&key={key}"
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        data = response.json()
        items = data.get('result', {}).get('items', [])  # Получаем список элементов
        if items:  # Проверяем, что список не пуст
            first_item = items[0]  # Берем первый элемент списка
            first_address = first_item.get('name', 'Название не найдено')  # Извлекаем название из первого элемента
            return first_address  # Возвращаем только первый адрес
        else:
            return 'Адрес не найден'  # Возвращаем сообщение об отсутствии адресов
    else:
        return 'Ошибка при получении адреса'  # Возвращаем сообщение об ошибке при запросе

