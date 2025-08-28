from app.infrastructure.db.session import engine

from app.models.dbModels import Base  # Base из dbModels для всех моделей.


def init_db():
    # Создает все таблицы в БД на основе моделей (Base.metadata — мета-данные таблиц).
    Base.metadata.create_all(bind=engine)
