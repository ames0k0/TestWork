# TestWork005
Микросервис анализа финансовых транзакций
1. Принимать транзакции через REST API
2. Сохранять транзакции в базу данных
3. Рассчитывать статистику и выполнять алгоритмическую обработку данных
4. Предоставлять результаты анализа через API

### Запуск приложения через Docker Compose
<details>
<summary>Зависимости</summary>
<pre>
docker -v   # Docker version 27.4.1, build b9d17ea
</pre>
</details>

```bash
docker compose up --build
```

- Документация будет доступно по ссылке: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)
  - `POST /transactions` - Загрузка транзакции
  - `DELETE /transactions` - Удаление всех транзакций
  - `GET /statistics` - Получение статистики по транзакциям

#### Запуск приложения локально (и тестирования)
> [!IMPORTANT]
> Необходимо редактировать ./deploy/.env-local

<details>
<summary>Зависимости</summary>
<pre>
psql -V           # psql (PostgreSQL) 15.7 (Ubuntu 15.7-0ubuntu0.23.10.1)
redis             # Redis Version: 7.4.1
celery --version  # 5.4.0 (opalescent)
python -V         # Python 3.11.6
pytest -V         # pytest 8.3.4
</pre>
</details>

```bash
# run redis service
service redis-server start

# run postgresql service
service postgresql start

# create venv
python -m venv .venv
pip install -r requirements.txt

# run rest api
fastapi dev run_restapi.py

# run analyser
celery -A run_analysis worker --loglevel=INFO

# run tests
pytest
```

---
<details>
<summary>Файловая структура проекта</summary>
<pre>
tree -a -I ".venv|__pycache__|__init__.py|.idea|.pytest_cache|data" --dirsfirst
.
├── analysis
│   └── app.py
├── deploy
│   ├── analysis
│   └── restapi
├── restapi
│   ├── app.py
│   ├── config.py
│   ├── connections.py
│   ├── crud.py
│   ├── models.py
│   └── schemas.py
├── tests
│   └── test_endpoints.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── run_analysis.py
└── run_restapi.py
</pre>
</details>

<details>
<summary>Использованные технологии</summary>
<ul>
  <li>FastAPI<sup>1</sup></li>
  <li>SQLAlchemy<sup>2</sup></li>
  <li>pytest<sup>3</sup></li>
  <li>PostgreSQL<sup>4</sup></li>
  <li>Redis<sup>5</sup></li>
  <li>Celery<sup>6</sup></li>
  <li>Docker Compose<sup>7</sup></li>
</ul>
</details>

#### Ссылки по технологиям
- <sup>1</sup>https://fastapi.tiangolo.com
- <sup>2</sup>https://www.sqlalchemy.org
- <sup>3</sup>https://docs.pytest.org/en/stable/
- <sup>4</sup>https://www.postgresql.org/
- <sup>5</sup>https://redis.io/
- <sup>6</sup>https://docs.celeryq.dev/en/stable/
- <sup>7</sup>https://docs.docker.com/compose
