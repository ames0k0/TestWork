# SMIT.studio

REST API сервис по расчёту стоимости страхование<br />
в зависимости от типа груза и объявленной стоимости (ОС)

### Развёртывание проекта в docker
<details>
<summary>Зависимости</summary>
<pre>
docker --version    # Docker version 27.3.1, build ce12230
poetry -V           # Poetry (version 1.8.3)
python -V           # Python 3.11.6
</pre>
</details>

```bash
docker build -t insurance-cost-rest-api .
docker run -p 8000:8000 -it insurance-cost-rest-api
```
- Будет доступно по ссылке: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)
  - `POST /` - Расчёт стоимости страхования
  - `GET /requests` - Запросы по расчёту стоимости страхования

### Запуск тестов проекта
```bash
poetry run pytest
```
- Тестов нужно запускать до работы с проектом (не разобрался с `conftest`)
  - Связано с тем, что есть тест на проверку файла с тарифом
  - Плюс, для теста и проекта используется одна база

---

<details>
<summary>Файловая структура проекта</summary>
<pre>
tree -a -I "__pycache__|__init__.py|.idea|.pytest_cache|data" --dirsfirst
.
├── src
│   ├── core
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   ├── lifespan.py
│   │   └── schemas.py
│   ├── database
│   │   ├── app.py
│   │   ├── crud.py
│   │   └── models.py
│   ├── static
│   │   └── sqlite3.db
│   ├── app.py
│   └── utils.py
├── tests
│   ├── conftest.py
│   └── test_app.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md
</pre>
</details>

<details>
<summary>Использованные технологии для разработки</summary>
<ul>
  <li>FastAPI<sup>1</sup></li>
  <li>SQLAlchemy<sup>2</sup></li>
  <li>sqlite3<sup>3</sup></li>
  <li>Pydantic<sup>4</sup></li>
</ul>
</details>

<details>
<summary>Использованные технологии для контейнеризации и изолированного запуска</summary>
<ul>
  <li>Docker<sup>5</sup></li>
</ul>
</details>

#### Ссылки по технологиям
- <sup>1</sup>https://fastapi.tiangolo.com
- <sup>2</sup>https://www.sqlalchemy.org
- <sup>3</sup>https://www.sqlite.org/docs.html
- <sup>4</sup>https://docs.pydantic.dev/latest
- <sup>5</sup>https://docs.docker.com

---
<p align="center"><img src="./data/rest-api.png" /></p>