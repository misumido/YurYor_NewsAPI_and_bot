import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")


API_SECRET_KEY = os.getenv("API_SECRET_KEY", "your_secret_key")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Путь к фотографиям
PHOTO_DIR = os.path.join(BASE_DIR, "photo")
os.makedirs(PHOTO_DIR, exist_ok=True)