### FastAPI + SQLAlchemy + sqlite3 (Backend Application and Database structure)

#### Start
```bash
# creating an environment
python3 -m venv env
source env/bin/activate

# installing the dependencies
pip install -r requirements.txt

# running the application
uvicorn src.run:app --reload
```

#### Dependencies
```bash
pip	-V		# 22.1.1
python	-V		# 3.10.5
sqlite3 --version	# 3.38.5
```

#### Project Structure
```
.
├── src
│   ├── backend
│   │   └── crud.py
│   └── sqldb
│       ├── database.py
│       ├── models.py
│       └── schemas.py
├── data
│   ├── sql_app_ignore-me.db
│   ├── star_wars_books.py
│   ├── star_wars_characters.py
│   └── star_wars_universe_locations.py
├── scripts
│   └── update_sqldb_data.py
├── README.md
├── requirements.txt
├── run.py
└── Task_ignore-me.pdf (4deeb72e505ff05d72b9bdd33dff4c16)
```

#### Application Structure (FastAPI)
```
/users/{user_id}	- GET	request	(Получение данных пользователя)
	>>> http://localhost:8000/users/1
	< {
	< 	"first_name": "Niv",
	< 	"last_name": "Lek",
	< 	"id": 1,
	< 	"email": "Lek.Niv@skeytracking.ru"
	< }

/users/{user_id}/orders	- GET	request (Просмотр истории заказов пользователя)
	>>> http://localhost:8000/users/1/orders
	< [
	<	{
	<		"reg_date": "2022-07-04T15:09:17.414040",
	<		"user_id": 1,
	<		"id": 1
	<	}
	<  ]

/users/{user_id}/order	- POST	request (Добавление нового заказа)
	>>> localhost:8000/users/1/order
	>>> {
	>>>     "books": [
	>>>         {
	>>>             "id": 1,
	>>>             "shop_id": 1,
	>>>             "quantity": 10
	>>>         }
	>>>     ]
	>>> }
	< null

/orders/{order_id}	- GET	request (Получение данных определенного заказа)
	>>> http://localhost:8000/orders/1
	< [
	< 	{
	< 		"id": 1,
	< 		"shop_id": 1,
	< 		"order_id": 1,
	< 		"book_id": 1,
	< 		"book_quantity": 10
	< 	}
	< ]

# try in the web at `http://localhost:8000/docs`
```

#### Script Structure (CLI) - Для создания и заполнения тестовой базы данных
```
script
	- scripts/update_sqldb_data.py
arguments
	--create-books N
	--create-shops N
	--create-orders N --order-items N
	--create-orders N --order-items start_N-stop_N		# random N between start_N and stop_N (ex. 3-9)
	--clear-tables all | users|books|shops|order_items	# delimiter ' '
example
	source env/bin/activate
	python scripts/update_sqldb_data.py --create-orders 2 --order-items 3-9
	python scripts/update_sqldb_data.py --clear-tables books shops
```
