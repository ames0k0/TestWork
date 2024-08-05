FROM python:3.11-alpine3.19

RUN mkdir build
COPY ./src/bot ./build
COPY ./src/bot/pyproject.toml ./src/web/poetry.lock* ./build/

WORKDIR /build

RUN pip3 install poetry && poetry lock --no-update && poetry install

CMD ["poetry", "run", "python", "main.py"]
