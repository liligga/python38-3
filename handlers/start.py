from aiogram import Router, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}, я бот. Напиши мне что-нибудь")