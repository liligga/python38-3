import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random


load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}, я бот. Напиши мне что-нибудь")


@dp.message(Command("pic"))
async def send_picture(message: types.Message):
    cat_pic = "images/cat.jpg"
    photo = types.FSInputFile(cat_pic)
    await message.answer_photo(photo=photo, caption="Котик")
    await message.reply_photo(photo=photo, caption="Котик")


@dp.message()
async def echo(message: types.Message):
    # print(message)
    await message.reply(message.text)


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="pic", description="Получить картинку")
    ])
    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())