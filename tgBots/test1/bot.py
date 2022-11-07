from aiogram import Bot, executor, Dispatcher, types
from config import TOKEN_API

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
 """

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(comands=['help'])
async def help_command(message: types.Message):
    await message.reply(text =HELP_COMMAND)

@dp.message_handler(comands=['start'])
async def help_command(message: types.Message):
    await message.answer(text = "Добро пожалавать в наш бот")
    await message.delete()# удаляет команду

if __name__ == "__main__":
    executor.start_polling(dp)
