from aiogram import Router, types
from aiogram.filters import Command
from datetime import datetime

from bot import bot, scheduler


scheduled_message_router = Router()

@scheduled_message_router.message(Command("later"))
async def send_later(message: types.Message):
    job_id = str(message.from_user.id)
    if job_id in scheduler.get_jobs():
        await message.answer("У вас уже есть запланированное напоминание! Для удаления напоминания введите /remove_later")
        return
    # scheduler.add_job(
    #     send_my_message,
    #     'interval',
    #     seconds=7,
    #     id=job_id,
    #     kwargs={'chat_id': message.from_user.id}
    # )
    # scheduler.add_job(
    #     send_my_message,
    #     'date',
    #     run_date=datetime(2024, 2, 23, 16, 22, 15),
    #     id=job_id,
    #     kwargs={'chat_id': message.from_user.id}
    # )
    scheduler.add_job(
        send_my_message,
        'cron',
        day_of_week='mon-fri',
        hour='17,19,21',
        minute=30,
        id=job_id,
        kwargs={'chat_id': message.from_user.id}
    )
    await message.answer("Будет сделано!")


@scheduled_message_router.message(Command("remove_later"))
async def remove_later(message: types.Message):
    job_id = str(message.from_user.id)
    if job_id in scheduler.get_jobs():
        scheduler.remove_job(job_id)
        await message.answer("Напоминание удалено!")


async def send_my_message(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="Напоминание ..."
    )