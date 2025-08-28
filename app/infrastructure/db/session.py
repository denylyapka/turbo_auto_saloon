from sqlalchemy import create_engine  # Для создания двигателя БД.

# Для сессий (транзакций).
from sqlalchemy.orm import sessionmaker, scoped_session

from app.infrastructure.core.config import settings  # Импорт настроек.

# Создаем engine — это подключение к БД из настроек (URI).
engine = create_engine(settings.ASYNC_DATABASE_URI)

# SessionLocal — фабрика для сессий (не коммитит автоматически).
SessionLocal = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))


def get_db():
    # Генератор для FastAPI — дает сессию для роутов, закрывает после использования.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
