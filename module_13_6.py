from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from Bubuka import Duduka

bot = Bot(token=Duduka)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.row(button1, button2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Выберите опцию:", reply_markup=kb)


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("Формула Миффлина-Сан Жеора для мужчин:"
                              "\n10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer(f"Введите свой рост(в см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer(f"Введите свой вес (в кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    bmr = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f"Ваша норма калорий: {bmr} ккал")
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    # print("Введите команду /start, чтобы начать общение.") Я учёл что нужно убрать принты
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
