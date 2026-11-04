import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


API_TOKEN = '' # Замените 'ВАШ_ТОКЕН_ЗДЕСЬ' на токен от BotFather

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    user_id = message.from_user.id
    await message.reply(f"Ваш Telegram ID: {user_id}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
