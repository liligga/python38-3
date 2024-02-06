from aiogram import Router, types
from aiogram.filters import Command
from pathlib import Path


picture_router = Router()

@picture_router.message(Command("pic"))
async def send_picture(message: types.Message):
    cat_pic = "images/cat.jpg"
    photo = types.FSInputFile(cat_pic)
    await message.answer_photo(photo=photo, caption="Котик")
    await message.reply_photo(photo=photo, caption="Котик")
