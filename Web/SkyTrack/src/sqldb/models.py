from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


# NOTES: added nullable=False but not `unique=True`


# User -> Order (One-to-Many)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    orders = relationship("Order")


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    reg_date = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("user.id"))


# OrderItem <- {Book,Shop} (Many-to-One)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)


class OrderItem(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("order.id"))
    order = relationship("Order")

    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book")

    shop_id = Column(Integer, ForeignKey("shop.id"))
    shop = relationship("Shop")

    book_quantity = Column(Integer, nullable=False)
