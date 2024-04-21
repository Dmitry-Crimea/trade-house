from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq


router = Router()

class ChooseProduct(StatesGroup):
    ProductCategory = State()
# class Reg(StatesGroup):
#     product_category = State ()
#     product_category = State()
#     city = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в торговый дом - "Славянский базар"!',
                             reply_markup=kb.main)


@router.callback_query(F.data == 'to_main')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в торговый дом - "Славянский базар"!',
                                reply_markup=kb.to_main)

#####################################################
#             Handler for products
#####################################################

@router.message(F.text == 'Товары')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию', reply_markup=await kb.products())


#####################################################
#             Handler for services
#####################################################

@router.message(F.text == 'Услуги')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию', reply_markup=await kb.services())

#####################################################
#             Handler for cities_products
#####################################################

@router.callback_query(F.data.startswith('product_'))
async def product(callback: CallbackQuery, state: FSMContext):
    product_category = callback.data.split('_')[1]
    await state.update_data(product_category=product_category)
    await callback.message.answer(f'Выбрана категория товара: {product_category}')
    await callback.message.answer('Выберите город',
                                  reply_markup=await kb.cities())

#####################################################
#             Handler for cities_service
#####################################################
@router.callback_query(F.data.startswith('service_'))
async def service(callback: CallbackQuery, state: FSMContext):
    service_category = callback.data.split('_')[1]
    await state.update_data(service_category=service_category)
    await callback.message.answer(f'Выбрана категория услуг: {service_category}')
    await callback.message.answer('Выберите город',
                                  reply_markup=await kb.cities())

#####################################################
#             Handler for item
#####################################################
@router.callback_query(F.data.startswith('city_'))
async def item(callback: CallbackQuery, state: FSMContext):
    city = callback.data.split('_')[1]
    data = await state.get_data()
    product_category = data.get('product_category')
    await callback.message.answer(f'Выбран город: {city}\nВыбрана категория: {product_category}')
    item_data = await rq.get_item(city, product_category)
    await callback.message.answer(f'Имя: {item_data}\n======================')
    await state.clear()
