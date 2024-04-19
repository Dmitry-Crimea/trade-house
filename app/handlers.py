import logging

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

logging.basicConfig(level=logging.INFO)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в торговый дом - "Славянский базар"!', reply_markup=kb.main)
    # await message.reply('Как дела!')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи!')

@router.message(F.text == 'Товары')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию товара', reply_markup =  await kb.kb_products())


@router.message(F.text == 'Услуги')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию услуг', reply_markup = await kb.kb_services())

###########################################
# CallBacks for Products && Services
###########################################

async def choose_city(callback: CallbackQuery):
    await callback.message.edit_text('Выберите город', reply_markup = await kb.kb_cities())

def product_callback(product_name: str):
    async def callback_func(callback: CallbackQuery):
        await choose_city(callback)
    return callback_func

def service_callback(service_name: str):
    async def callback_func(callback: CallbackQuery):
        await choose_city(callback)
    return callback_func

# Callbacks for products
product_names = ['Продовольственные товары', 'Бытовая химия', 'Стройматериалы', 'Автозапчасти']
for product_name in product_names:
    callback_name = f'product_{product_name}'
    callback_func = product_callback(product_name)
    router.callback_query(F.data == callback_name)(callback_func)

# Callbacks for services
service_names = ['СТО', 'Юридические услуги', 'Строительство', 'Тепло/водоснабжение', 'Электрика']
for service_name in service_names:
    callback_name = f'service_{service_name}'
    callback_func = service_callback(service_name)
    router.callback_query(F.data == callback_name)(callback_func)