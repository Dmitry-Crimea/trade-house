from sqlalchemy import select

from app.database.models import async_session
from app.database.models import User, Product, Item, City, Service

async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_products():
    async with async_session() as session:
        return await session.scalars(select(Product))

async def get_services():
    async with async_session() as session:
        return await session.scalars(select(Service))

async def get_cities():
    async with async_session() as session:
        return await session.scalars(select(City))

async def get_product_item(product_name):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.product == product_name))

async def get_city_item(city_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.city == city_id))

async def get_service_item(service_name):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.service == service_name))

# async def get_item(item_id):
#     async with async_session() as session:
#         return await session.scalar(select(Item).where(Item.city == item_id))

# async def get_item(city, product):
#     async with async_session() as session:
#         return await session.scalar(select(Item).where(Item.city == city, Item.product == product))


async def get_item(city, product):
    async with async_session() as session:
        item = select(Item).where(Item.city == city, Item.product == product)
        result = await session.execute(item)
        items = result.fetchall()
        return items