from aiogram import Router, F, types
from aiogram.filters import Command


group_admin_router = Router()
BAD_WORDS = ("дурак", "тупой")


@group_admin_router.message(Command("ban", prefix="!"), F.chat.type == "group")
async def ban_user(message: types.Message):
    # print("TEXT: ", message.text, "\nFROM: ", message.from_user, "\nREPLY: ", message.reply_to_message)
    if message.reply_to_message is not None:
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
        )
        await message.answer("Пользователь забанен")


# "Ты тупой дурак"
@group_admin_router.message(F.chat.type == "group")
async def catch_bad_words(message: types.Message):
    # print("CHAT TYPE:", message.chat.type)
    text = message.text.lower()
    for word in BAD_WORDS:
        if word in text:
            await message.answer("Нельзя так выражаться")
            await message.delete()
            break

