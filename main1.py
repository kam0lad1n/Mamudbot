# from aiogram import Bot, Dispatcher, types
# from aiogram.enums import ParseMode
# from aiogram.filters import Command
# import asyncio
#
# API_TOKEN = '8040675229:AAEYq6zLeRYfM5Rs61e1GOtpcfqxEeiNhMA'
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot=bot)
#
#
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     # check_sub_chanel = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
#     # if check_sub_chanel.status in ["member", "administrator", "creator"]:
#     await message.answer("Botdan foydalanish mumkin✅\nYordam olish uchun: /help" )
#     # else:
#     #     await message.answer("Botdan foydalanish uchun kanalga obuna bo'ling✅")
# @dp.message(Command("help"))
# async def help(message: types.Message):
#     # check_sub_chanel = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
#     # if check_sub_chanel.status in ["member", "administrator", "creator"]:
#     await message.answer("Botdan foydalanish:", parse_mode=ParseMode.HTML)
#
# @dp.message()
# async def check(message: types.Message):
#     data = message.text
#
#     if data == "1":
#         media = open("image.", "rb")
#         bot.send_
#
# async def main():
#     print("Bot ishga tushdi...")
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     asyncio.run(main())
