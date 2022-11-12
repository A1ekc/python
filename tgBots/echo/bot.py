from aiogram.types import Message#импортируем тип message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio

from config import BOT_TOKEN
from config import admin_id# для того чтобы себе отпрвлять сообщения

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)

async def send_to_admin(dp):
    await bot.send_message(chat_id = admin_id, text = 'Бот запущен')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! \nНапиши мне что - нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_comand(message: types.Message):
    await message.reply("Напиши мне что - нибудь, и я отправлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo(message: Message):# тип сообщения Message тип сообщения импортировали ранее из iogram 
    text = f"Привет, ты написал :{message.text}"
    await bot.send_message(chat_id=message.from_user.id,text = text)# отвечаем сообщением пользователю

if __name__ == '__main__':# постоянный опрос сервера на наличие сообщений
    executor.start_polling(dp)





