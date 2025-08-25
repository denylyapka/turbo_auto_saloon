from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.core.config import settings

# Создание движка
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,  # можно включить True для логов SQL
    future=True  # новый API SQLAlchemy 2.0
)

# Фабрика сессий
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)


# Зависимость для FastAPI / общего использования
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
