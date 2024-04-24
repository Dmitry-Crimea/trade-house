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

async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))

async def get_item_product(city, product_category):
    async with async_session() as session:
        result = await session.scalars(select(Item).where((Item.city == city) &
                                                          (Item.product == product_category)))
        return result

async def get_item_service(city, service_category):
    async with async_session() as session:
        result = await session.scalars(select(Item).where(Item.city == city,
                                                          Item.service == service_category))
        return result
