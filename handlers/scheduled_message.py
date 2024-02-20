from aiogram import Router, types
from aiogram.filters import Command

from bot import bot, scheduler


scheduled_message_router = Router()

@scheduled_message_router.message(Command("later"))
async def send_later(message: types.Message):
    scheduler.add_job(
        send_my_message,
        'interval',
        seconds=7,
        kwargs={'chat_id': message.from_user.id}
    )
    await message.answer("Будет сделано!")


async def send_my_message(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="Напоминание ..."
    )