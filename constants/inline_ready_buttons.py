from kbds.inline import get_callback_buttons

MAIN_MENU = get_callback_buttons(
    buttons={
        'Хочу узнать больше!': 'show_info',
        'Основы КПТ': 'tasks',
        'Чат с Асей': 'chat_with_bot',
        '🏥️Найти ближайший центр психологической помощи 🏥️': 'find_clinic',
        'Экстренная помощь': 'extra_help',
        'О боте': 'about_bot',
    },
    sizes=(1, 1, 1, 1),
)

RETURN_TO_MENU = get_callback_buttons(buttons={'Вернуться в меню': 'back_to_menu'})

YES_OR_NO = get_callback_buttons(buttons={'Да!': 'answer_yes', 'Нет.': 'back_to_menu'})

STAGES = get_callback_buttons(
    buttons={
        'Первый шаг': 'tasks_step_one',
        'Второй шаг': 'tasks_step_two',
        'Третий шаг': 'tasks_step_three',
    },
    sizes=(1, 1, 1),
)
