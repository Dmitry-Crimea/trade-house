from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_products, get_product_item, get_city_item, get_cities, get_services

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Товары')],
                                     [KeyboardButton(text='Услуги')],
                                     [KeyboardButton(text='О проекте')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

to_main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='На главную',
                                                                      callback_data='to_main')]])


#####################################################
#             Keyboard for products
#####################################################
async def products():
    all_products = await get_products()
    keyboard = InlineKeyboardBuilder()

    for product in all_products:
        keyboard.add(InlineKeyboardButton(text=product.name, callback_data=f'product_{product.name}'))
    return keyboard.adjust(1).as_markup()

#####################################################
#             Keyboard for cities
#####################################################
async def cities():
    all_cities = await get_cities()
    keyboard = InlineKeyboardBuilder()

    for city in all_cities:
        keyboard.add(InlineKeyboardButton(text=city.name, callback_data=f'city_{city.name}'))
    return keyboard.adjust(2).as_markup()

#####################################################
#             Keyboard for services
#####################################################
async def services():
    all_services = await get_services()
    keyboard = InlineKeyboardBuilder()

    for service in all_services:
        keyboard.add(InlineKeyboardButton(text=service.name, callback_data=f'service_{service.name}'))
    return keyboard.adjust(1).as_markup()

#####################################################
#             Keyboard for item
#####################################################
async def items(city_id):
    all_items = await get_city_item(city_id)
    keyboard = InlineKeyboardBuilder()

    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))

    return keyboard.adjust(1).as_markup()

