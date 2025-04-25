import os

from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

load_dotenv()

scheduler = BackgroundScheduler()
scheduler.start()

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": os.getenv("DB_NAME"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD"),
                "port": os.getenv("DB_PORT"),
                "host": os.getenv("DB_HOST"),
                "statement_cache_size": 0,
            },
        }
    },
    "apps": {
        "models": {
            "models": [
                "app.models.restaurant",
                "aerich.models",
            ],
            "default_connection": "default",
        }
    },
}
