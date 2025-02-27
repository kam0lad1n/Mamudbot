import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# Bot token from BotFather
TOKEN = "7966762210:AAFg42j0V8n-THgwNY5FdUchVe39N9scVjQ"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Replace with your name
YOUR_NAME = "Jasurbek"

@dp.message()
async def respond_to_name(message: Message):
    if message.text.strip().lower() == YOUR_NAME.lower():
        await message.reply(f"Salom, {YOUR_NAME}! Sizni ko'rib turganimdan xursandman! 😊")
    else:
        await message.reply("Kechirasiz, men faqat ma'lum ismga javob beraman.")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "main":
    asyncio.run(main())
