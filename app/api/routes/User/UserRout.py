from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.user import create_user, get_user_by_id, update_user, delete_user, get_hashed_password, get_user_by_email

from app.models.dtoModels.UserDTO import UserDTO, UserEditDTO

from .utils.hash_password import hashing_password

router = APIRouter()


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_user_by_id(user_id=id, session=session)
    return data

@router.get("/password/{email}")
async def get_hashed_password_def(email: str, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_hashed_password(email=email, session=session)
    return data

@router.get("/email/{email}")
async def get_by_email(email: str, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_user_by_email(email=email, session=session)
    return data


@router.post("/add_user")
async def add_user(user: UserDTO, session: AsyncSession = Depends(fastapi_get_db)):
    # Хешируем пароль (например, с помощью библиотеки `passlib`)
    hashed_password = hashing_password(user.password)
    
    # Преобразуем Pydantic-модель в ваш датакласс `UserInput`
    user_data = UserDTO(
        name=user.name,
        surname=user.surname,
        patronymic=user.patronymic,
        dateborn=user.dateborn,
        email=user.email,
        password=hashed_password,
    )
    data = await create_user(user_data=user_data, session=session)
    return data


@router.put("/")
async def update(user: UserEditDTO, session: AsyncSession = Depends(fastapi_get_db)):
    data = await update_user(user=user, session=session)
    return data


@router.delete("/{id}")
async def delete(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    data = await delete_user(user_id=id, session=session)
    return data
