import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from app.database import SessionLocal
from app import models

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    args = message.text.split(maxsplit=1)
    chat_id = str(message.chat.id)

    if len(args) < 2:
        await message.answer("Привет! Перейдите по ссылке из вашего аккаунта, чтобы привязать Telegram.")
        return

    code = args[1]
    db = SessionLocal()

    link_code = db.query(models.TelegramLinkCode).filter(models.TelegramLinkCode.code == code).first()

    if not link_code:
        await message.answer("Код недействителен или уже использован.")
        db.close()
        return

    user = db.query(models.User).filter(models.User.id == link_code.user_id).first()
    user.telegram_chat_id = chat_id
    username = user.username

    db.delete(link_code)
    db.commit()
    db.close()

    await message.answer(f"Готово! Telegram привязан к аккаунту {username}.")


async def main():
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())