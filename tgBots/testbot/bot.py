from email import message
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

bot = Bot(TOKEN_API)
# Диспетчер
dp = Dispatcher(bot)


@dp.message_handler()# ответ - текст пользователя в верхнем регистре
async def echo_capitalize(message: types.Message):
    await message.answer(text=message.text.capitalize())

if __name__ =='__name__':
    executor.start_polling(dp)
