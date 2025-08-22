from sqlalchemy import Column, Integer, String, Text, Float, ARRAY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 82.1: Services (Услуги)


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    short_description = Column(Text)
    description = Column(Text)
    price = Column(Float)
    time_action = Column(Integer)
    photos = Column(ARRAY(String))  # Массив строк, например, URL фото

# 82.2: Companies (Компании)


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300))
    short_description = Column(Text)
    description = Column(Text)
    # Массив строк, например, ["Пн-Пт: 9-18", "Сб: 10-15"]
    working_hours = Column(ARRAY(String))

# 82.3: CrossReference (услуги + компании) - многие-ко-многим


class ServiceCompany(Base):
    __tablename__ = "service_companies"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    service_id = Column(Integer, ForeignKey("services.id"))

# 82.4: CategoriesServices (Категории услуг)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(200))

# 82.5: CrossReference (категории) - иерархия категорий


class CategoryHierarchy(Base):
    __tablename__ = "category_hierarchies"
    id = Column(Integer, primary_key=True, index=True)
    parent_category = Column(Integer, ForeignKey("categories.id"))
    child_category = Column(Integer, ForeignKey("categories.id"))
