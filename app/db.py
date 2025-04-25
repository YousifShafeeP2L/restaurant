import logging

from app.config import TORTOISE_ORM
from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")


def init_db(app: FastAPI):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def close_db():
    await Tortoise.close_all_connections()
    log.info("DB connection closed")
