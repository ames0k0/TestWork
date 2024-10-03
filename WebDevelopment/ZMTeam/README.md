# ZM Team

Тестовое задания (TO-DO Приложение)
- `backend` для создание и обновлений задач
- `bot` для уведомления о состояние задач

### Запуск `backend`
```commandline
docker compose up --build
```
- Доступно по ссылке: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)
  - `POST /tasks/create`- Создание задачи
  - `GET  /tasks/list`- Предоставляет весь список задач
  - `GET  /tasks/<task_id>` - Данные по конкретной задаче
  - `POST /tasks/<task_id>/update` - Обновление данные задачи

<details>
<summary>Зависимости</summary>
<pre>
docker --version        # Docker version 27.2.1, build 9e34c9b
poetry -V               # Poetry (version 1.8.3)
poetry run python -V    # Python 3.11.6
</pre>
</details>

<details>
<summary>Файловая Структура</summary>
<pre>
tree -a -I "__pycache__|__init__.py|.idea"
.
├── backend
│   ├── Dockerfile
│   ├── .env
│   ├── main.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── src
│       ├── core
│       │   ├── config.py
│       │   └── dependencies.py
│       ├── endpoints
│       │   ├── main.py
│       │   └── tasks
│       │       ├── crud.py
│       │       ├── models.py
│       │       ├── router.py
│       │       └── schemas.py
│       ├── main.py
│       └── sql
│           └── db.py
├── bot
├── database
│   └── .env
├── docker-compose.yml
└── README.md
</pre>
</details>

## Задание 1
> Сервис кастомных нотификации через телеграм

Бесконечный цикл для поиска задач, для уведомления о состоянии задач

- Зависимости
  - database (backend)
- Технологии
  - sqlalchemy+postgresql
  - aiogram
  - asyncio
- Слабые стороны
  - Монолит
- Сильные стороны
  - Асинхронность

## Задание 2
> Бэкенд сервиса “To Do” для отслеживания задач

- Замечание
    - без тестов и документации