import logging
from contextlib import asynccontextmanager

from app.api import restaurant_api
from app.db import close_db, init_db
from app.helper_classes.exception_handler import CustomError
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    yield
    await close_db()


def create_application() -> FastAPI:
    application = FastAPI(lifespan=lifespan_handler)
    application.include_router(restaurant_api.router)
    return application


app = create_application()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(CustomError)
async def custom_error_handler(request: Request, exc: CustomError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error = exc.errors()[0]
    error_key = error["loc"][-1].replace("_", " ")
    error_message = (
        error["msg"]
        .replace("match pattern '^(", "be ")
        .replace(")$'", "")
        .replace("|", ", ")
        .lower()
    )
    error_messages = {"error": f"{error_key} {error_message}"}
    return JSONResponse(status_code=400, content=error_messages)


log = logging.getLogger("uvicorn")

init_db(app)
