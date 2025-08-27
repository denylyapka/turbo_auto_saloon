import logging  # Комментарий: Для базового логирования ошибок и инфо.

import uvicorn  # Комментарий: Сервер для запуска FastAPI.

from environs import Env  # Комментарий: Для чтения .env — настройки БД и т.д.

# Комментарий: Классы FastAPI для роутов и запросов.
from fastapi import APIRouter, FastAPI, HTTPException, Request

# Комментарий: Импорт твоего api_router с роутерами.
from app.api.main import api_router

# Комментарий: Глобальный обработчик ошибок (добавь файл ниже).
from app.infrastructure.exception_handler import global_exception_handler

# Комментарий: Инициализация БД (создание таблиц).
from app.infrastructure.init_db import init_db

# Комментарий: Твой логгер (добавь файл ниже, если нет).
from app.infrastructure.logger import logger


# Комментарий: Читаем .env файл для настроек.
env = Env()
env.read_env()


# Комментарий: Настраиваем базовый уровень логирования (INFO — для инфо сообщений).
logging.basicConfig(level=logging.INFO)


# Комментарий: Главный роутер — включает api_router.
main_router = APIRouter()
main_router.include_router(api_router)


# Комментарий: Создаем приложение FastAPI.
app = FastAPI()


# Комментарий: Подключаем главный роутер с префиксом /api.
app.include_router(main_router, prefix="/api")


# Комментарий: Добавляем глобальный обработчик ошибок.
app.add_exception_handler(Exception, global_exception_handler)


# Комментарий: Middleware — функция, которая выполняется для каждого запроса (логирует запрос и ответ).
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Комментарий: Логируем запрос.
    logger.info(f"Request: {request.method} {request.url}")
    # Комментарий: Вызываем следующий handler (роут).
    response = await call_next(request)
    # Комментарий: Логируем статус ответа.
    logger.info(f"Response status: {response.status_code}")
    return response


# Комментарий: Обработчик для HTTPException (ошибки вроде 404).
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # Комментарий: Логируем ошибку.
    logger.error(f"HTTP Exception: {exc.detail} - {exc.status_code}")
    # Комментарий: Вызываем глобальный handler.
    return await global_exception_handler(request, exc)


# Комментарий: Событие при запуске — инициализируем БД (async, если проект async).
@app.on_event("startup")
async def on_startup():
    await init_db()  # Комментарий: Создаем таблицы в БД.


# Комментарий: Если запускаем файл напрямую — стартуем сервер uvicorn.
if __name__ == "__main__":
    # Комментарий: Запуск на локалхост:5000.
    uvicorn.run(app, host="127.0.0.1", port=5000)
