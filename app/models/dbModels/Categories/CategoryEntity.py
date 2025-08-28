# Импорты для колонок (id — целое, category_name — строка).
from sqlalchemy import Column, Integer, String

from app.models.dbModels.base import Base  # Импорт Base.

# Класс модели для категории (82.4) — представляет таблицу in БД.


class CategoryEntity(Base):
    __tablename__ = "categories"  # Имя таблицы в БД.

    # ID — первичный ключ, с индексом для быстрого поиска.
    id = Column(Integer, primary_key=True, index=True)
    # Имя категории, строка до 200 символов (как в схеме).
    category_name = Column(String(200))

    def __init__(self, **kwargs):
        # Конструктор — позволяет создавать объект как CategoryEntity(category_name="Test"). kwargs — словарь аргументов, setattr устанавливает атрибуты.
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        # Конвертирует объект в словарь для вывода (например, {'id': 1, 'category_name': 'Test'}). Полезно для API или логов.
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
