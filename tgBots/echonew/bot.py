from aiogram import Bot, Dispatcher, executor, types


# бот - сервер, который будет взаимодествовать с API Telegram

TOKEN_API = "5796388825:AAEESPCqa7Kj8YQH2FbtNDcuRbdS87-865Y"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)#ответить на сообщение



if __name__ == '__main__':
    executor.start_polling(dp)# запуск бота




