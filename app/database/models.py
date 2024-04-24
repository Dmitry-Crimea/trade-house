from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from typing import List
from config import ENGINE, ECHO

engine = create_async_engine(url=ENGINE, echo=ECHO)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

    item_rel: Mapped['Item'] = relationship(back_populates='city_rel')

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

    item_rel: Mapped[List['Item']] = relationship(back_populates='product_rel')

class Service(Base):
    __tablename__ = 'services'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

    item_rel: Mapped[List['Item']] = relationship(back_populates='service_rel')

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    summary: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(120))
    phone: Mapped[str] = mapped_column(String(25))
    product: Mapped[str] = mapped_column(ForeignKey('products.name'), nullable=True)
    service: Mapped[str] = mapped_column(ForeignKey('services.name'), nullable=True)
    city: Mapped[str] = mapped_column(ForeignKey('cities.name'))

    city_rel: Mapped['City'] = relationship(back_populates='item_rel')
    product_rel: Mapped['Product'] = relationship(back_populates='item_rel')
    service_rel: Mapped['Service'] = relationship(back_populates='item_rel')


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)