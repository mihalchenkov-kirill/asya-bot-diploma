from kbds.inline import get_callback_buttons

MAIN_MENU = get_callback_buttons(buttons={'Хочу узнать больше!': 'show_info', 'О боте': 'about_bot'}, sizes=(1, 1))

RETURN_TO_MENU = get_callback_buttons(buttons={'Вернуться в меню': 'back_to_menu'})

YES_OR_NO = get_callback_buttons(buttons={'Да!': 'answer_yes', 'Нет.': 'back_to_menu'})
