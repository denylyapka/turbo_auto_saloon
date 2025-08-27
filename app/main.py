import logging  # Логирование

import uvicorn

from environs import Env

# Классы FastAPI для роутов и запросов.
from fastapi import APIRouter, FastAPI, HTTPException, Request

from app.api.main import api_router

from app.infrastructure.exception_handler import global_exception_handler

# Инициализация БД
from app.infrastructure.init_db import init_db

from app.infrastructure.logger import logger


env = Env()
env.read_env()


logging.basicConfig(level=logging.INFO)


main_router = APIRouter()
main_router.include_router(api_router)

app = FastAPI()

app.include_router(main_router, prefix="/api")


app.add_exception_handler(Exception, global_exception_handler)


# Middleware — функция, которая выполняется для каждого запроса (логирует запрос и ответ).
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Логируем запрос.
    logger.info(f"Request: {request.method} {request.url}")
    # Вызываем следующий handler (роут).
    response = await call_next(request)
    # Логируем статус ответа.
    logger.info(f"Response status: {response.status_code}")
    return response


# Обработчик для HTTPException (ошибки вроде 404).
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # Логируем ошибку.
    logger.error(f"HTTP Exception: {exc.detail} - {exc.status_code}")
    # Вызываем глобальный handler.
    return await global_exception_handler(request, exc)


# Событие при запуске — инициализируем БД (async, если проект async).
@app.on_event("startup")
async def on_startup():
    await init_db()  # Создаем таблицы в БД.


# Если запускаем файл напрямую — стартуем сервер uvicorn.
if __name__ == "__main__":
    # Запуск на локалхост:5000.
    uvicorn.run(app, host="127.0.0.1", port=5000)
