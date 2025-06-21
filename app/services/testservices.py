import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.UserRepository import UserRepository
from app.models.dbModels.User.UserEntity import UserEntity as User

# Import your repositories and entities


async def get_user_by_id(user_id: int, session: AsyncSession) -> User:
    repo_user = UserRepository(session)
    return await repo_user.get_by_id(user_id=user_id)

async def test_service(session: AsyncSession) -> Any:
    repo_user = UserRepository(session)

    user = User(
        name="Test", surname="Testovich",
        datetime_reg=datetime.datetime.now(),
        email="email", hashed_password="secret"
    )

    data = await repo_user.create(user=user)

    return data
