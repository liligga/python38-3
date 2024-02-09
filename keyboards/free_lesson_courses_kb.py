from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def free_lesson_courses_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Бекенд"),
                KeyboardButton(text="Фронтенд"),
            ],
            [
                KeyboardButton(text="Android"),
                KeyboardButton(text="IOs"),
            ],
            [
                KeyboardButton(text="Тестирование"),
            ]
        ],
        resize_keyboard=True
    )
    return kb
