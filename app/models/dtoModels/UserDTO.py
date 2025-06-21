from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    """Базовая схема пользователя (без идентификатора и секретных данных)"""
    name: str
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    dateborn: datetime
    email: EmailStr

class UserCreate(UserBase):
    """Схема для создания пользователя (с паролем)"""
    hashed_password: str

class UserDTO(UserBase):
    """Основная DTO схема пользователя (с идентификатором)"""
    id: int
    datetime_reg: datetime

    class Config:
        from_attributes = True  # Для совместимости с ORM (ранее orm_mode = True)

class UserResponse(UserDTO):
    """Схема для ответа API (может быть расширена)"""
    pass

class UserWithSecret(UserDTO):
    """Схема с секретными данными (только для внутреннего использования)"""
    hashed_password: str