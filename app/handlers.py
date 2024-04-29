from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq
from app.database.requests import (get_products, get_cities, get_services,get_item_product,
                                   get_item_products, get_item_service, get_item_services)

router = Router()

# class ChooseProduct(StatesGroup):
#     ProductCategory = State()
class Reg(StatesGroup):
    product_category = State ()
    service_category = State()
    city = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в торговый дом - "Славянский базар"!',
                             reply_markup=kb.main)


@router.callback_query(F.data == 'to_main')
async def cmd_start(message: Message):
    await message.answer('Вы вернулись на главную')
    await message.answer('Добро пожаловать в торговый дом - "Славянский базар"!',
                                reply_markup=kb.main)


@router.message(F.text == '🛒 Товары')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию', reply_markup=await kb.products())



@router.message(F.text == '🛠️ Услуги')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию', reply_markup=await kb.services())

@router.message(F.text == '💼 Вакансии')
async def cmd_test(message: Message):
    await message.answer('Данный раздел находится в разработке...')


@router.callback_query(F.data.startswith('product_'))
async def product(callback: CallbackQuery, state: FSMContext):
    product_category = callback.data.split('_')[1]
    await state.update_data(product_category=product_category)
    await callback.message.answer(f'Выбрана категория товара: {product_category}')
    await callback.message.answer('Выберите город',
                                  reply_markup=await kb.cities())
    await callback.message.delete()


@router.callback_query(F.data.startswith('service_'))
async def service(callback: CallbackQuery, state: FSMContext):
    service_category = callback.data.split('_')[1]
    await state.update_data(service_category=service_category)
    await callback.message.answer(f'Выбрана категория услуг: {service_category}')
    await callback.message.answer('Выберите город',
                                  reply_markup=await kb.cities())
    await callback.message.delete()


@router.callback_query(F.data.startswith('city_'))
async def item(callback: CallbackQuery, state: FSMContext):
    city = callback.data.split('_')[1]
    data = await state.get_data()
    # await state.update_data(city=city)

    if 'product_category' in data:
        product_category = data.get('product_category')
        items = await get_item_product(city, product_category)
        if items:
            await callback.message.answer(f'Выберите поставщика:',
                                          reply_markup=await kb.items_product(city, product_category))
        else:
            await callback.message.answer(f"В этом городе пока нет товаров для данной категории")

    elif 'service_category' in data:
        service_category = data.get('service_category')
        items = await get_item_service(city, service_category)
        if items:
            await callback.message.answer(f'Выберите поставщика:',
                                           reply_markup=await kb.items_service(city, service_category))
        else:
            await callback.message.answer(f"В этом городе пока нет услуг для данной категории")
    else:
         await callback.message.answer (f"В этом городе пока нет товаров или услуг для данной категории")
    await state.clear()
    await callback.message.delete()


@router.callback_query(F.data.startswith('item_'))
async def item(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.message.answer(f'======================'
                                  f'\nИмя: {item_data.name}'
                                  f'\n\nОписание: {item_data.description}'
                                  f'\n\nТелефон: {item_data.phone}'
                                  f'\n======================')
    await callback.message.delete()
