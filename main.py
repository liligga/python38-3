import asyncio
from aiogram import types
import logging
from bot import bot, dp
from handlers import (
    start_router,
    picture_router,
    echo_router,
    courses_router
)


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="pic", description="Получить картинку"),
        types.BotCommand(command="courses", description="Наши курсы"),
    ])
    # добавляем роутеры
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(courses_router)

    # в самом конце
    dp.include_router(echo_router)

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    # включаем логи
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())