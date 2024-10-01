FROM python:3.11.6-slim

WORKDIR /code

COPY poetry.lock pyproject.toml /code

RUN pip3 install "poetry==1.8.3"
RUN poetry install

COPY . /code

EXPOSE 8000

CMD ["poetry", "run", "python", "main.py"]