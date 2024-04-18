from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Товары')],
                                     [KeyboardButton(text='Услуги')],
                                     [KeyboardButton(text='О проекте')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

products = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Продовольственные товары', callback_data='food_producrts')],
    [InlineKeyboardButton(text='Бытовая химия', callback_data='household_chemicals')],
    [InlineKeyboardButton(text='Стройматериалы', callback_data='building_materials')],
    [InlineKeyboardButton(text='Автозапчасти', callback_data='auto parts')]])
#
# food_producrts = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Мясо', callback_data='meat')],
#     [InlineKeyboardButton(text='Рыба и морепродукты', callback_data='fish_and_seafood')],
#     [InlineKeyboardButton(text='Овощи и фрукты', callback_data='vegetables_and_fruits')],
#     [InlineKeyboardButton(text='Кисломолочные продукты', callback_data='milk_products')],
#     [InlineKeyboardButton(text='Мед', callback_data='honey')]])
#
# building_materials = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Внутренняя отделка')],
#     [InlineKeyboardButton(text='Кровля и фасад')],
#     [InlineKeyboardButton(text='Фундамент')],
#     [InlineKeyboardButton(text='Лаки/краски')]])
#
services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='СТО', callback_data='service_station')],
    [InlineKeyboardButton(text='Юридические услуги', callback_data='legal_services')],
    [InlineKeyboardButton(text='Строительство', callback_data='construction')],
    [InlineKeyboardButton(text='Тепло/водоснабжение', callback_data='heat_water_supply')],
    [InlineKeyboardButton(text='Электрика', callback_data='electrics')]])
#
# Города


cities = ['Алупка', 'Алушта', 'Армянск', 'Балаклава',
          'Балаклава', 'Бахчисарай', 'Белогорск', 'Евпатория',
          'Керч', 'Саки', 'Севастополь', 'Симферополь',
          'Судак', 'Черноморское', 'Ялта']

async def user_cities():
    keyboard = InlineKeyboardBuilder()
    for city in cities:
        keyboard.add(InlineKeyboardButton(text=city, callback_data=f'city_{city}'))
    return keyboard.adjust(3).as_markup()

