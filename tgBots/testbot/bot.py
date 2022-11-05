from aiogram.types import Message#импортируем тип message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN_API
from config import admin_id# для того чтобы себе отпрвлять сообщения
import asyncio

loop = asyncio.get_event_loop()#Создаём поток где будут обрабатываться все события
bot = Bot(TOKEN_API)
# Диспетчер
#dp = Dispatcher(bot)# экземпляр класса
dp = Dispatcher(bot, loop=loop)#Создаём обработчик и доставщик/ Берём бота и полученный поток


async def send_to_admin(dp):
    await bot.send_message(chat_id = admin_id, text = 'Бот запущен')


@dp.message_handler()# ответ - текст пользователя в верхнем регистре
async def echo_upper(message: types.Message):#принимаем сообщение
    if message.text.count(' ') >= 1:# ответит ответным сообщением если в приёмном сообщении будет хотя бы один пробел
        await message.answer(text=message.text.upper())# ответ

if __name__ =='__name__':
    executor.start_polling(dp)#polling запрос сервера на обновлние данных
