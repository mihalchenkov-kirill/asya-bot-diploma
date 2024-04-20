from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Перезапустить бота'),
        ],
        {KeyboardButton(text='🏥️Найти ближайший центр психологической помощи 🏥️️', request_location=True)},
        {
            KeyboardButton(text='Показать меню'),
            KeyboardButton(text='О боте'),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?',
)

del_kbd = ReplyKeyboardRemove()
