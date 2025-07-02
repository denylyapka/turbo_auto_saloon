from typing import Optional, List
from datetime import datetime

from app.models.dbModels.User.UserEntity import UserEntity


class IUserRepository:
    async def create(self, user: UserEntity) -> UserEntity:
        """Создать нового пользователя"""
        raise NotImplementedError("Метод не вызван!")

    async def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        """Получить пользователя по ID"""
        raise NotImplementedError("Метод не вызван!")

    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        """Получить пользователя по email"""
        raise NotImplementedError("Метод не вызван!")

    async def get_all(self) -> List[UserEntity]:
        """Получить всех пользователей"""
        raise NotImplementedError("Метод не вызван!")

    async def update(self, id: int, user: UserEntity) -> UserEntity:
        """Обновить данные пользователя"""
        raise NotImplementedError("Метод не вызван!")

    async def delete(self, user_id: int) -> bool:
        """Удалить пользователя по ID"""
        raise NotImplementedError("Метод не вызван!")
    
    async def get_hashed_password_by_email(self, email: str) -> Optional[str]:
        """Получить хэшированный пароль по email"""
        raise NotImplementedError("Метод не вызван!")

    async def search(
            self,
            name: Optional[str] = None,
            surname: Optional[str] = None,
            email: Optional[str] = None,
            dateborn_from: Optional[datetime] = None,
            dateborn_to: Optional[datetime] = None,
            datetime_reg_from: Optional[datetime] = None,
            datetime_reg_to: Optional[datetime] = None
    ) -> List[UserEntity]:
        """Поиск пользователей по параметрам"""
        raise NotImplementedError("Метод не вызван!")