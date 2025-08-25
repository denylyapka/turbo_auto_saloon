from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.main import api_router
from app.infrastructure.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # код при запуске приложения
    init_db()   # если функция синхронная
    # await init_db()  # если функция асинхронная
    yield
    # код при завершении приложения (например, закрыть соединение)

app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api")
