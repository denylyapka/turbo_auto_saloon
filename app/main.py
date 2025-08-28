import logging  # Для логгирования
import uvicorn  # Для запуска сервера
from environs import Env  # Для .env
from contextlib import asynccontextmanager

# FastAPI
from fastapi import APIRouter, FastAPI, HTTPException, Request

# Импорт твоих модулей
from app.api.main import api_router
from app.infrastructure.exception_handler import global_exception_handler
from app.infrastructure.init_db import init_db
from app.infrastructure.logger import logger


# Читаем .env
env = Env()
env.read_env()

# Базовая настройка логгирования (уровень INFO)
logging.basicConfig(level=logging.INFO)


# Lifespan — новый способ инициализации при запуске/остановке приложения
# Почему то старый у меня не работает, @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    # При старте приложения
    await init_db()
    yield
    # При завершении (если надо закрыть соединение с БД — здесь)


# Создаем приложение
app = FastAPI(lifespan=lifespan)

# Главный роутер — включает api_router
main_router = APIRouter()
main_router.include_router(api_router)

# Подключаем роутер с /api
app.include_router(main_router, prefix="/api")

# Глобальный обработчик ошибок
app.add_exception_handler(Exception, global_exception_handler)


# Middleware — логирует каждый запрос
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


# Обработчик для HTTP ошибок
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Exception: {exc.detail} - {exc.status_code}")
    return await global_exception_handler(request, exc)


# Если запускаем файл напрямую — стартуем uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
