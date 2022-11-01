from aiogram.types import Message
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Включаем логгирование чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token = "5796388825:AAEESPCqa7Kj8YQH2FbtNDcuRbdS87-865Y")
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message(commands = ['Start'])
async def cmd_start(message: types.Message):
    await message.answer('Hello!')

#Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

# хендлер на команду /test1
@dp.message(comands=['test1'])
async def cmd_test1(message: types.Message):
    await message.reply('Test 1')
# хендлер на команду /test1
@dp.message(comands=['test2'])
async def cmd_test1(message: types.Message):
    await message.reply('Test 2')
