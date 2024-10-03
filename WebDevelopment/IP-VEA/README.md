# Messaging Application (без Плюсов)
Позволяет создавать (написать) анонимных сообщений. [ТЗ](./data/TODO)
- Стэк: Nginx/Unit + FastAPI + MongoDB + aiogram3

### Web приложение (FastAPI)
- Реализован ендпоинты
  - `GET    /api/v1/messages`- показывает список всех сообщений (limit=20)
  - `POST   /api/v1/message`- позволяет написать сообщение
  - `DELETE /api/v1/messages` - позволяет удалять всех сообщений

### Телеграм бот (aiogram3)
> Все "текст" сообщение будут создаваться.
> Отправляет запросы на web приложение
- Реализован команды
  - `/start` - Приветствие
  - `/messages` - показывает список всех сообщений (limit=20)
  - `/delete` - позволяет удалять всех сообщений

## Как запускать (необходимо токен бота)
```bash
echo 'BOT_TOKEN={TelegramBotToken}' > ./src/bot/.env

docker-compose up
```

## Замечание
- Не стал создавать переменных как `MONGO_DSN=`, `WEB_APP_ENDPOINT=`
- Приложение развертывается на `localhost` (network_mode=host)
```
MONGO_DSN="mongodb://root:toor@localhost:27017/"
WEB_APP_ENDPOINT="http://localhost:80/api/v1"
```

## Скрины
### Web
![Web](./data/WEB.png)
### Bot
![Bot](./data/BOT.png)
