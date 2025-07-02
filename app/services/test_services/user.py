import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.UserRepository import UserRepository
from app.models.dbModels.User.UserEntity import UserEntity as User


async def create_user(user_data, session: AsyncSession) -> Any:
    repo_user = UserRepository(session)

    user = User(
        name=user_data.name,
        surname=user_data.surname,
        patronymic=user_data.patronymic,
        dateborn=user_data.dateborn,
        datetime_reg=datetime.datetime.now(),
        email=user_data.email,
        hashed_password=user_data.password
    )
    data = await repo_user.create(user=user)
    return data


async def get_user_by_id(user_id: int, session: AsyncSession) -> User:
    repo_user = UserRepository(session)
    return await repo_user.get_by_id(user_id=user_id)

async def get_user_by_email(email: str, session: AsyncSession) -> User:
    repo_user = UserRepository(session)
    return await repo_user.get_by_email(email=email)

async def get_all(session: AsyncSession) -> Any:
    repo_user = UserRepository(session)
    return await repo_user.get_all()

async def get_hashed_password(email: str, session: AsyncSession) -> Any:
    repo_user = UserRepository(session)
    return await repo_user.get_hashed_password_by_email(email=email)


async def update_user(user: User, session: AsyncSession) -> Any:
    repo_user = UserRepository(session)
    return await repo_user.update(id=user.id, user=user)


async def delete_user(user_id: int, session: AsyncSession) -> Any:
    repo_user = UserRepository(session)
    return await repo_user.delete(user_id=user_id)
