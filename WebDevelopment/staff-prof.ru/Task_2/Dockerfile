FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY app .
EXPOSE 8000

CMD [ "fastapi", "dev", "--host", "0.0.0.0", "./main.py" ]