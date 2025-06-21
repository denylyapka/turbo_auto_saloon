from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.User.UserEntity import UserEntity as User
from typing import List, Optional
from datetime import datetime

from app.models.dbModels.User.IUserRepository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        """Создать нового пользователя"""
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_by_id(self, user_id: int) -> Optional[User]:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        user = result.scalars().first()
        return user.to_dict() if user else None

    async def get_by_email(self, email: str) -> Optional[User]:
        """Получить пользователя по email"""
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self) -> List[User]:
        """Получить всех пользователей"""
        query = select(User)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update(self, user: User) -> User:
        """Обновить данные пользователя"""
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete(self, user_id: int) -> bool:
        """Удалить пользователя по ID"""
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        user = result.scalar_one_or_none()

        if user:
            await self.session.delete(user)
            await self.session.commit()
            return True
        return False

    async def search(
            self,
            name: Optional[str] = None,
            surname: Optional[str] = None,
            email: Optional[str] = None,
            dateborn_from: Optional[datetime] = None,
            dateborn_to: Optional[datetime] = None,
            datetime_reg_from: Optional[datetime] = None,
            datetime_reg_to: Optional[datetime] = None
    ) -> List[User]:
        """Поиск пользователей по параметрам"""
        query = select(User)

        filters = {
            'name': (User.name.ilike, f"%{name}%"),
            'surname': (User.surname.ilike, f"%{surname}%"),
            'email': (User.email.ilike, f"%{email}%"),
            'dateborn_from': (User.dateborn >= dateborn_from),
            'dateborn_to': (User.dateborn <= dateborn_to),
            'datetime_reg_from': (User.datetime_reg >= datetime_reg_from),
            'datetime_reg_to': (User.datetime_reg <= datetime_reg_to)
        }

        for param, (condition, value) in filters.items():
            if value is not None:
                query = query.where(condition(value))

        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_hashed_password(self, username: str) -> Optional[str]:
        """Получить хэшированный пароль по имени пользователя"""
        query = select(User.hashed_password).where(User.name == username)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()