from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Наш Инстаграм", url="https://instagram.com/")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ]
        ]
    )
    await message.answer(f"Привет, {message.from_user.first_name}, я бот.", reply_markup=kb)


@start_router.callback_query(F.data == "about_us")
async def show_about_us(cb: types.cbQuery):
    await cb.answer()
    await cb.message.answer("Что-то о нас")