## MVP Project
<h5>Поставленные задачи к проекту</h5>
<ul>
  <li>Реализовать API для сохранения резюме и имя претендента</li>
  <li>Реализовать систему рейтинга для резюме проставляемого пользователем</li>
</ul>

<h5>Использованные технологии для разработки</h5>
<ul>
  <li>FastAPI</li>
  <li>PostgreSQL</li>
  <li>SQLAlchemy</li>
  <li>Pydantic</li>
</ul>

<h5>Использованные технологии для контейнеризации и изолированного запуска</h5>
<ul>
  <li>Docker</li>
  <li>Docker Compose</li>
</ul>

## Запуск проекта
<details>
<summary>Зависимости проекта</summary>
<pre>
docker --version        # Docker version 27.2.1, build 9e34c9b
poetry -V               # Poetry (version 1.8.3)
poetry run python -V    # Python 3.11.6
</pre>
</details>

<details>
<summary>Файловая структура проекта</summary>
<pre>
tree -a -I "__pycache__|__init__.py|.idea" --dirsfirst
.
├── data
│   ├── api.png
│   └── ProjectStructure.drawio
├── secret
│   ├── .env-backend
│   └── .env-postgresql
├── src
│   ├── resume
│   │   ├── crud.py
│   │   ├── enums.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── utils.py
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   ├── lifespan.py
│   └── main.py
├── static
│   ├── docs
│   │   └── ProjectStructure.drawio.png
│   └── resume
├── docker-compose.yml
├── Dockerfile
├── main.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── md5sum(Task.txt) -> 425f4ea9633ec41cc120f1b236c4fcf0
</pre>
</details>

```bash
docker compose up --build
```
- Проект будет доступно по ссылке: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)
  - `POST /upload/` - Принимает файл и имя претендента, сохраняет их
  - `POST /delete/<resume_id>/` - Удаляет резюме из базы и удаляет файл
  - `POST /vote/` - Увеличивает голоса (`vote_count`) резюме
  - `GET /list/` - Выводит пагинированный список резюме

## Замечание от автора проекта
- Система рейтинга реализован через ендпоинт `/vote/`
  - Доступно через ендпоинт `/list/`
    - передачей Query-параметра `order_by=vote_count`
- `APIDOG` не был заполнен и передан
- Ендпоинт `/list/` не выдаёт ID резюме
- Резюме из папки `static` доступно по `/static/`
  - `/code/static/resume/<filename>`
  - `http://0.0.0.0:8000/static/resume/<filename>`
  - Будут не доступны после завершения проекта

---
<p align="center"><img src="./data/api.png" /></p>