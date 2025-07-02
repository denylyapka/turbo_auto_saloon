import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.UserRepository import UserRepository
from app.models.dbModels.User.UserEntity import UserEntity as User


async def get_user_by_id(user_id: int, session: AsyncSession) -> User:
    repo_user = UserRepository(session)
    return await repo_user.get_by_id(user_id=user_id)

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
