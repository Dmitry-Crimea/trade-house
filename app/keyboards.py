from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Товары')],
                                     [KeyboardButton(text='Услуги')],
                                     [KeyboardButton(text='О проекте')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


###########################################
# Keyboard for products
###########################################
products = ['Продовольственные товары', 'Бытовая химия',
            'Стройматериалы','Автозапчасти']
async def kb_products():
    keyboard = InlineKeyboardBuilder()
    for product in products:
        keyboard.add(InlineKeyboardButton(text=product, callback_data=f'product_{product}'))
    return keyboard.adjust(1).as_markup()

###########################################
# Keyboard for services
###########################################
services = ['СТО', 'Юридические услуги', 'Строительство',
            'Тепло/водоснабжение', 'Электрика']

async def kb_services():
    keyboard = InlineKeyboardBuilder()
    for service in services:
        keyboard.add(InlineKeyboardButton(text=service, callback_data=f'service_{service}'))
    return keyboard.adjust(1).as_markup()


###########################################
# Keyboard for Cities
########################################### 
cities = ['Алупка', 'Алушта', 'Армянск', 'Балаклава',
          'Балаклава', 'Бахчисарай', 'Белогорск', 'Евпатория',
          'Керч', 'Саки', 'Севастополь', 'Симферополь',
          'Судак', 'Черноморское', 'Ялта']

async def kb_cities():
    keyboard = InlineKeyboardBuilder()
    for city in cities:
        keyboard.add(InlineKeyboardButton(text=city, callback_data=f'city_{city}'))
    return keyboard.adjust(3).as_markup()

