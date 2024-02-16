from aiogram import Router, F, types
from aiogram.filters import Command
from bot import db


courses_router = Router()

@courses_router.message(Command("courses"))
async def show_all_courses(message: types.Message):
    # courses = db.get_courses()
    # for course in courses:
    #     await message.answer(f"Название курса: {course[1]}\nОписание: {course[2]}")
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Python"),
                types.KeyboardButton(text="FrontEnd"),
            ],
            [
                types.KeyboardButton(text="Android"),
                types.KeyboardButton(text="IOs"),
            ],
            [
                types.KeyboardButton(text="Тестирование"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Выберите направление из меню нмже", reply_markup=kb)


@courses_router.message(F.text.lower() == "python")
async def show_python(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Что-то о нашем направлении по Python", reply_markup=kb)


@courses_router.message(F.text.lower() == "frontend")
async def show_python(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Что-то о нашем направлении по Front End", reply_markup=kb)