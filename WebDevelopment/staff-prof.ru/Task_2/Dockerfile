FROM alpine:3.21.3

RUN apk add --no-cache ffmpeg python3 py3-pip

WORKDIR /app
COPY requirements.txt .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY app .
EXPOSE 8000

CMD [ "fastapi", "dev", "--host", "0.0.0.0", "./main.py" ]