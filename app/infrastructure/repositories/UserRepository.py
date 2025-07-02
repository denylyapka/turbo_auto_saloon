from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.User.UserEntity import UserEntity as User
from typing import List, Optional
from datetime import datetime

from app.models.dbModels.User.IUserRepository import IUserRepository

from app.api.routes.User.utils.hash_password import hashing_password


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
        users = result.scalars().all()
        return [user.to_dict() for user in users] if users else []

    async def get_all(self) -> List[User]:
        """Получить всех пользователей"""
        query = select(User)
        result = await self.session.execute(query)
        users = result.scalars().all()
        return [user.to_dict() for user in users] if users else []

    async def update(self, id: int, user: User) -> User:
        """Обновить данные пользователя"""
        # 1. Получаем пользователя из базы
        db_user = await self.session.get(User, id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # 2. Обновляем только изменяемые поля
        update_data = user.dict(exclude_unset=True)
        for field, value in update_data.items():
            if field == 'password' and value:  # Особый случай для пароля
                setattr(db_user, 'hashed_password', hashing_password(value))
            elif hasattr(db_user, field):  # Обновляем только существующие атрибуты
                setattr(db_user, field, value)
        
        # 3. Сохраняем изменения
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        
        return db_user

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
        users = result.scalars().all()
        return [user.to_dict() for user in users] if users else []

    async def get_hashed_password_by_email(self, email: str) -> Optional[str]:
        """Получить хэшированный пароль по email"""
        query = select(User.hashed_password).where(User.email == email)
        result = await self.session.execute(query)
        user = result.scalars().first()
        return user if user else None
