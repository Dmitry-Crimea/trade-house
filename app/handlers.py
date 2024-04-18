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
    await message.answer('Выберите категорию товара', reply_markup =  kb.products)

@router.message(F.text == 'Услуги')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию услуг', reply_markup =  kb.services)

@router.callback_query(F.data == 'food_producrts')
async def food_producrts(callback: CallbackQuery):
    # await callback.answer('Выберите город', show_alert=True)
    await callback.message.edit_text('Выберите город', reply_markup = await kb.user_cities())


# @router.callback_query(F.data == 'household_chemicals')
# async def household_chemicals(callback: CallbackQuery):
#     await callback.answer('Вы выбрали категорию товара "Бытовая химия"', show_alert=True)
#     await callback.message.answer('Вы выбрали категорию товара "Бытовая химия"')
#
# @router.callback_query(F.data == 'building_materials')
# async def building_materials(callback: CallbackQuery):
#     await callback.answer('Вы выбрали категорию товара "Строительные материалы"', show_alert=True)
#     await callback.message.answer('Вы выбрали категорию товара "Строительные материалы"')