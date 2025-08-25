from sqlalchemy.orm import Session
from app.infrastructure.db.session import engine
from app.models.dbModels import Base


def init_db(db: Session = None):
    # Создаём таблицы (если их ещё нет)
    Base.metadata.create_all(engine)
