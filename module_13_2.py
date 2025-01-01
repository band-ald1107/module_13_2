from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
import asyncio

api = "8034211613:AAGwwI_HNkzXCQfDDEx7YNuiZoLvp3Vcrps"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')

# Функция для обработки всех остальных сообщений
@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)