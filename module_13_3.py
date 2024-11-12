from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "8076338165:AAHMBPpsra0lfvBHA9r0RXyUqBXZteHRIyE"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(massage):
    print("Привет! Я бот помогающий твоему здоровью.")
    await massage.answer("Привет! Я бот помогающий твоему здоровью.")
@dp.message_handler()
async def all(massage):
    print("Введите команду /start, чтобы начать общение.")
    await  massage.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__" :
    executor.start_polling(dp, skip_updates=True)