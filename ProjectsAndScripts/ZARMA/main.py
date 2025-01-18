#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = "ames0k0"

import sqlite3
from pathlib import Path
from urllib.request import urlretrieve


def connect_and_download_web_data():
    """ Подключение к API и получение данных

    Сохраните полученные данные в формате JSON в файл
    """
    output_filename = DATA_DIR / "web_content.json"

    urlretrieve(
        url="https://jsonplaceholder.typicode.com/posts",
        filename=output_filename
    )


def print_db_users_over_thirty():
    """ Обработка данных с использованием SQL

    Выбор всех пользователей старше 30 лет и выводит их имена и возраст
    """
    database_filename = DATA_DIR / "users.db"

    conn = sqlite3.connect(database_filename)
    curr = conn.cursor()

    curr.execute(
        "SELECT name, age FROM users where age > 30"
    )

    longest_russian_name = "Staronizhestebliyevskaya"
    for name, age in curr.fetchall():
        print(f"name={name:<{len(longest_russian_name)}} {age=}")

    # Example Output:
    # name=alex                     age=39
    # name=anna                     age=31
    # name=bob                      age=33


def combining_data_from_different_sources():
    """ Объединение данных из разных источников

    Скрипт должен объединить данные по product_id и вывести итоговую таблицу,
        с информацией о продажах для каждого продукта.

    Первый источник - это CSV-файл с информацией о продуктах
        (поля: product_id, product_name)
    Второй источник - это JSON-файл с данными о продажах
        (поля: sale_id, product_id, amount)
    """
    # Hashmap, I'll use a Hashmap! (c) Joma Tech
    data = {}
    csv_data = []
    json_data = [{}]

    for product_id, product_name in csv_data:
        # NOTE: not checked for a duplicates
        data[product_id] = {
            "product_name": product_name,
            "sales_amount": 0
        }

    for sale in json_data:
        product_id = sale["product_id"]
        amount = sale["sales_amount"]
        if product_id not in data:
            continue
        data[product_id]["sales_amount"] += amount

    print("ProductID  | SalesAmount | ProductName")
    print("-----------+-------------+------------")
    for product_id, product_sale in data.items():
        product_name = product_sale["product_name"]
        sales_amount = product_sale["sales_amount"]
        print(f"{product_id:<10} | {sales_amount:<11} | {product_name}")

    # Example output:
    # ProductID  | SalesAmount | ProductName
    # -----------+-------------+------------
    # 1          | 20          | Test product


def optimized_script():
    """ Оптимизация скрипта

    numbers = [(i ** 2) for i in range(1, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    """
    squares = [(i ** 2) for i in range(1, 1000001)]


if __name__ == "__main__":
    DATA_DIR = Path("DATA")
    DATA_DIR.mkdir(exist_ok=True)

    # connect_and_download_web_data()
    # print_db_users_over_thirty()
    # combining_data_from_different_sources()
    # optimized_script()
