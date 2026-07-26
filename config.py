import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parent / ".env")

DB_URL = os.getenv("DB_URL") or os.getenv("DATABASE_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")

if not DB_URL:
    raise RuntimeError("DB_URL is not set. Add it to .env or environment variables.")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. Add it to .env or environment variables.")
