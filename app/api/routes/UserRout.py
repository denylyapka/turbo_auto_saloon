from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.user import create_user, get_user_by_id

router = APIRouter()


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_user_by_id(user_id=id, session=session)
    return data


from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class UserInputRequest(BaseModel):
    name: str
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    dateborn: Optional[date] = None
    email: EmailStr  # автоматическая валидация email
    password: str  # открытый пароль (не хешированный!)


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


@router.post("/add_user")
async def add_user(user_input: UserInputRequest, session: AsyncSession = Depends(fastapi_get_db)):
    # Хешируем пароль (например, с помощью библиотеки `passlib`)
    hashed_password = hash_password(user_input.password)
    
    # Преобразуем Pydantic-модель в ваш датакласс `UserInput`
    user_data = UserInputRequest(
        name=user_input.name,
        surname=user_input.surname,
        patronymic=user_input.patronymic,
        dateborn=user_input.dateborn,
        email=user_input.email,
        password=hashed_password,
    )
    print("user_data:", user_data)
    data = await create_user(user_data=user_data, session=session)
    return data
