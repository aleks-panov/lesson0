from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kbi = InlineKeyboardMarkup()
kbi2 = InlineKeyboardMarkup()
bt1 = KeyboardButton(text="Рассчитать")
bt2 = KeyboardButton(text="Информация")
bt3 = KeyboardButton(text="Купить")
bti1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
bti2 = InlineKeyboardButton(text="Формулы расчета", callback_data="formulas")
bti3 = InlineKeyboardButton(text="Product 1", callback_data="product_buying")
bti4 = InlineKeyboardButton(text="Product 2", callback_data="product_buying")
bti5 = InlineKeyboardButton(text="Product 3", callback_data="product_buying")
bti6 = InlineKeyboardButton(text="Product 4", callback_data="product_buying")
kb.add(bt1)
kb.add(bt2)
kb.add(bt3)
kbi.add(bti1)
kbi.add(bti2)
kbi2.add(bti3)
kbi2.add(bti4)
kbi2.add(bti5)
kbi2.add(bti6)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(massage):
    await massage.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb)

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kbi)

@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 * вес в кг + 6.25 * рост в см - 5 * возраст + 5")
    await call.answer()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()


@dp.message_handler(text="Рассчитать")
async def count(message):
    await message.answer("Введите свой возраст")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer("ВВедите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    cal = int(10 * int(data['third']) + 6.25 * int(data['second']) - 5 * int(data['first']) + 5)
    await message.answer(f"Ваша норма калорий {cal}")
    await state.finish()

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    with open("product1.jpeg", "rb") as img:
        await message.answer_photo(img, "Продукт 1")
    with open("product2.jpg", "rb") as img:
        await message.answer_photo(img, "Продукт 2")
    with open("product3.jpeg", "rb") as img:
        await message.answer_photo(img, "Продукт 3")
    with open("product4.jpg", "rb") as img:
        await message.answer_photo(img, "Продукт 4")
    await message.answer("Выберите продукт для покупки", reply_markup=kbi2)

@dp.callback_query_handler(text="product_buying")
async def set_age(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
