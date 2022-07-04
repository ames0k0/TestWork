import os
import sys
import random
import argparse
from typing import Optional, NoReturn
from datetime import datetime

sys.path.append(os.getcwd())

from src.sqldb.database import SessionLocal
from src.sqldb.models import User, Book, Shop, Order, OrderItem

from data.star_wars_books import sw_books
from data.star_wars_characters import sw_names
from data.star_wars_universe_locations import sw_universe_locations


def clear_test_tables(clear_tables: list[str]) -> None:
    """Cleans tables by name or with flag 'all'
    """
    tables = [User, Book, Shop, Order, OrderItem]

    if 'all' in clear_tables:
        for table in tables:
            db.query(table).delete()
        clear_tables.clear()

    for table in clear_tables:
        if table == 'users':
            db.query(User).delete()
        elif table == 'books':
            db.query(Book).delete()
        elif table == 'shops':
            db.query(Shop).delete()
        elif table == 'order_items':
            db.query(Order).delete()
            db.query(OrderItem).delete()

    db.commit()


def create_random_datetime() -> datetime:
    """Creates random datetime
    """
    # example: 2022-07-03 21:06:51
    year = random.randint(1500, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    # h/m/s is not needed
    hours = random.randint(0, 23)
    minutes = random.randint(1, 60)
    seconds = random.randint(1, 60)
    return datetime(year, month, day, hours, minutes, seconds)


def create_user() -> tuple[str]:
    """Generates user data
    """
    first_name = random.choice(sw_names).split(' ', maxsplit=1)

    if len(first_name) == 2:
        first_name, last_name = first_name
    else:
        first_name = first_name[0]
        last_name = 'Mars'

    # FIXFOR: 'SAN LOR TEKKA'
    last_name = last_name.replace(' ', '-')

    first_name, last_name = [s.title() for s in (first_name, last_name)]
    email = f"{first_name}.{last_name}@skeytracking.ru"

    return (last_name, first_name, email)


def create_test_users(create_users: int) -> None:
    """Creates N *User
    """
    for _ in range(create_users):
        last_name, first_name, email = create_user()

        # FIXFOR(hack): `unique=True` (SQLAlchemy.exc.IntegrityError)
        db_user_by_email = db.query(User).filter(email==email).first()
        if db_user_by_email:
            random_age = random.randint(1000, 500_000)
            email = f"{random_age}-{email}"

        db_user = User(last_name=last_name, first_name=first_name, email=email)
        db.add(db_user)
    db.commit()


def create_test_books(create_books: int) -> None:
    """Creates N *Book
    """
    for _ in range(create_books):
        book = random.choice(sw_books)
        name, author = book
        release_date = create_random_datetime()
        db_book = Book(name=name, author=author, release_date=release_date)
        db.add(db_book)
    db.commit()


def create_test_shops(create_shops: int) -> None:
    """Creates N *Shop
    """
    for _ in range(create_shops):
        universe_location = random.choice(sw_universe_locations)
        name, address = universe_location
        db_shop = Shop(name=name, address=address)
        db.add(db_shop)
    db.commit()


def create_test_orders_with_random_items(create_orders: int, order_items: str) -> Optional[NoReturn]:
    """Creates N *Order with N or random N of range(N-N) *OrderItem
    """
    max_users = db.query(User).count()
    max_books = db.query(Book).count()
    max_shops = db.query(Shop).count()

    if not max_users:
        print('Create users first')
        tearDown()
    if not max_books:
        print('Create books first')
        tearDown()
    if not max_shops:
        print('Create shops first')
        tearDown()

    order_items = order_items.split('-')

    a, b = 0, 0
    default_a = '1'

    if len(order_items) == 1:
        order_items = order_items[0]
        a = int(order_items if order_items.isdigit() else default_a)
    elif len(order_items) == 2:
        a, b = order_items
        a, b = [int(s if s.isdigit() else default_a) for s in (a, b)]
        if not b:
            print("Set positive number for order items range")
            tearDown()
    else:
        a = int(default_a)

    # True
    user = db.query(User).filter(User.first_name==User.first_name).first()
    books = db.query(Book).filter(Book.name==Book.name).limit(DATABASE_SELECT_MAX_ROWS).all()
    shops = db.query(Shop).filter(Shop.name==Shop.name).limit(DATABASE_SELECT_MAX_ROWS).all()

    for _ in range(create_orders):
        db_order = Order(user_id=user.id)
        db.add(db_order)
        db.commit()

        local_a = a

        if b:
            local_a = random.randint(a, b)

        added_items = 0

        for _ in range(DATABASE_SELECT_MAX_ROWS):
            if added_items == local_a:
                break

            if not books:
                break

            book = books.pop()

            for shop in shops:
                book_quantity = random.randint(1, DATABASE_SELECT_MAX_ROWS)

                order_item = OrderItem(
                    order_id=db_order.id, book_id=book.id,
                    shop_id=shop.id, book_quantity=book_quantity
                )
                db.add(order_item)

                added_items += 1

        db.commit()


if __name__ == '__main__':
    DATABASE_SELECT_MAX_ROWS = 10

    def only_positive_numbers(value):
        value = int(value)
        if value <= 0:
            raise argparse.ArgumentTypeError("%s is not a positive integer" % value)
        if value > DATABASE_SELECT_MAX_ROWS:
            raise argparse.ArgumentTypeError("%s - must be <= 10" % value)
        return value

    parser = argparse.ArgumentParser()
    # N-users
    parser.add_argument('--create-users', help="Create N users", type=only_positive_numbers)

    # N-books
    parser.add_argument('--create-books', help="Create N books", type=only_positive_numbers)

    # N-shops
    parser.add_argument('--create-shops', help="Create N shops", type=only_positive_numbers)

    # --create-orders N --order-items (N|range N-N)
    parser.add_argument('--create-orders', help="Create N orders", type=only_positive_numbers)
    parser.add_argument('--order-items',
                        help="Create N order items OR items with ragne N-N if setted --create-order",
                        type=str)
    parser.add_argument('--clear-tables',
                        help="Deletes all data from tables: users, books, shops, orders_items, all",
                        choices=['users', 'books', 'shops', 'order_items', 'all'],
                        nargs='+', type=str)

    args = parser.parse_args()

    create_users = args.create_users
    create_books = args.create_books
    create_shops = args.create_shops
    create_orders = args.create_orders
    order_items = args.order_items
    clear_tables = args.clear_tables

    if not any((create_users, create_books, create_shops, create_orders, order_items, clear_tables)):
        parser.print_help()
        exit()

    db = SessionLocal()

    def tearDown():
        db.close()
        exit()

    if clear_tables:
        clear_test_tables(clear_tables)
    if create_users:
        create_test_users(create_users)
    if create_books:
        create_test_books(create_books)
    if create_shops:
        create_test_shops(create_shops)

    orders = (create_orders, order_items)

    if all(orders):
        create_test_orders_with_random_items(create_orders, order_items)
    elif any(orders):
        print("Example of use:")
        print("\t--create-orders 1 --order-items 5")
        print("\t--create-orders 2 --order-items 2-9")
        tearDown()
