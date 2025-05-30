# 📰 YurYor News API

REST API на FastAPI для получения информации о новостях, опубликованных в Telegram канале. Новости управляются через бота на aiogram, а API предоставляет доступ к опубликованному контенту.

## ✨ Функциональность

- **Получение новостей**: API для доступа к опубликованным новостям
- **Фотографии новостей**: загрузка и получение изображений к новостям
- **Фильтрация**: пагинация и поиск по ID новости или message_id
- **Авторизация**: защита API с помощью токенов
- **Telegram интеграция**: управление новостями через Telegram бота
- **База данных**: хранение новостей с использованием SQLAlchemy ORM

## 🛠️ Технологии

- **Python 3.12**
- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy** - ORM для работы с базой данных
- **SQLite** - база данных для хранения новостей
- **aiogram** - для управления новостями через Telegram бота
- **Pydantic** - валидация данных и схемы ответов

## 🚀 Установка и запуск

### Обычный запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/misumido/yuryornews_api.git
cd YurYorNewsAPI_BOT
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте переменные окружения в файле `.env`:
```
DATABASE_URL=sqlite:///./news.db
TELEGRAM_API_TOKEN=your_telegram_bot_token
TELEGRAM_CHANNEL_ID=-100xxxxxxxxx
API_SECRET_KEY=your_api_secret_key
```

4. Запустите API:
```bash
python main.py
```

5. Запустите Telegram бота:
```bash
python run.py
```

### 🐳 Запуск через Docker

1. Соберите образ:
```bash
docker build -t yuryornews_api .
```

2. Запустите контейнер:
```bash
docker run -d --name yuryornews_api --env-file .env -p 8000:8000 yuryornews_api
```

## 📁 Структура проекта

```
YurYorNewsAPI_BOT/
├── database/              # Модули для работы с базой данных
│   ├── __init__.py
│   ├── adminservice.py    # Административные функции
│   ├── botservice.py      # Сервисы для бота
│   ├── models.py          # Модели SQLAlchemy
│   └── newsservice.py     # Сервисы для работы с новостями
├── newsbot/               # Telegram бот
│   ├── buttons.py         # Клавиатуры и кнопки
│   ├── news_bot.py       # Основная логика бота
│   └── states.py         # Состояния бота
├── photo/                # Директория для хранения фотографий
├── .env                  # Переменные окружения
├── configs.py           # Конфигурационные файлы
├── main.py              # FastAPI приложение
├── news.db              # База данных SQLite
├── run.py               # Запуск Telegram бота
├── schemas.py           # Pydantic схемы
├── Dockerfile           # Docker конфигурация
└── requirements.txt     # Python зависимости
```

## 🔗 API Endpoints

- `GET /api/news` - Получить все опубликованные новости
- `GET /api/news/{news_id}` - Получить новость по ID
- `GET /api/news/message/{message_id}` - Получить новость по message_id
- `GET /api/news/photo/{news_id}` - Получить фотографию новости

API документация доступна по адресу: `http://localhost:8000/`

## 👨‍💻 Автор

**GitHub**: [@misumido](https://github.com/misumido)  
**Telegram**: [@medical_ninja](https://t.me/medical_ninja)