from aiogram import Router, types


echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    # print(message)
    await message.reply(message.text)