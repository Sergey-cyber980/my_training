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

# Кнопка "Купить" в главном меню
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(KeyboardButton("Рассчитать"), KeyboardButton("Купить"))

# Inline-меню для продуктов
kb_products = InlineKeyboardMarkup(resize_keyboard=True)
kb_products.add(
    InlineKeyboardButton(text="Product1", callback_data="product_buying"),
    InlineKeyboardButton(text="Product2", callback_data="product_buying"),
    InlineKeyboardButton(text="Product3", callback_data="product_buying"),
    InlineKeyboardButton(text="Product4", callback_data="product_buying")
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=kb_main)

@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора для мужчин:"
                              "\n10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer(f"Введите свой рост(в см):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer(f"Введите свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    bmr = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f"Ваша норма калорий: {bmr} ккал")
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
        await bot.send_photo(chat_id=message.chat.id, photo=open(f"D:/PythonProjecst/TelegramBot/files/{i}.png", 'rb'))
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_products)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")

@dp.message_handler()
async def all_massages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)