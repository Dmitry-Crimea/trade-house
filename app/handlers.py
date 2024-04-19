import logging

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

logging.basicConfig(level=logging.INFO)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в торговый дом - "Славянский базар"!', reply_markup=kb.main)


@router.message(F.text == 'Товары')
async def cmd_test(message: Message):
    await message.answer('Выберите категорию', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.message.answer('выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price} р.',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))