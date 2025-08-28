# Импорт для создания Base.
from sqlalchemy.ext.declarative import declarative_base

# Создаём Base — все модели наследуются от него, чтобы SQLAlchemy знал, что это таблицы БД. Это фундамент для всех таблиц.
Base = declarative_base()
