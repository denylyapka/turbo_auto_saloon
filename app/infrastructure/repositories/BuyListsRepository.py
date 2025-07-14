from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from datetime import datetime
from app.models.dbModels.BuyLists.BuyListsEntity import BuyListsEntity
from app.models.dbModels.BuyLists.IBuyListsRepository import IBuyListsRepository

class BuyListsRepository(IBuyListsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, buy_list: BuyListsEntity) -> dict:
        try:
            self.session.add(buy_list)
            await self.session.commit()
            await self.session.refresh(buy_list)
            return buy_list.to_dict()
        except Exception as e:
            await self.session.rollback()
            raise ValueError(f"Failed to create buy list: {str(e)}") from e

    async def get_by_id(self, list_id: int) -> Optional[BuyListsEntity]:
        query = select(BuyListsEntity).where(BuyListsEntity.id == list_id)
        result = await self.session.execute(query)
        buy_list = result.scalars().first()
        return buy_list.to_dict() if buy_list else None
    
    async def get_by_id_inner(self, list_id: int) -> Optional[BuyListsEntity]:
        query = select(BuyListsEntity).where(BuyListsEntity.id == list_id)
        result = await self.session.execute(query)
        buy_list = result.scalars().first()
        return buy_list

    async def get_by_type(self, list_type: str) -> List[BuyListsEntity]:
        query = select(BuyListsEntity).where(BuyListsEntity.type == list_type)
        result = await self.session.execute(query)
        buy_lists = result.scalars().all()
        return [buy_list.to_dict() for buy_list in buy_lists]

    async def get_all(self) -> List[BuyListsEntity]:
        query = select(BuyListsEntity)
        result = await self.session.execute(query)
        buy_lists = result.scalars().all()
        return [buy_list.to_dict() for buy_list in buy_lists]
    
    async def get_products_by_buy_list_id(self, buy_list_id: int) -> List[BuyListsEntity]:
        query = select(BuyListsEntity).where(BuyListsEntity.id == buy_list_id)
        result = await self.session.execute(query)
        buy_list = result.scalars().first()
        products = buy_list.to_dict()["products"]
        return products

    async def update(self, buy_list: BuyListsEntity) -> dict:
        # Получаем текущую запись
        existing = await self.get_by_id_inner(buy_list.id)
        if not existing:
            return None
            
        # Обновляем поля
        existing.type = buy_list.type
        existing.products = existing.products + buy_list.products
        existing.total_price = buy_list.total_price
        existing.total_discount = buy_list.total_discount
        
        await self.session.commit()
        await self.session.refresh(existing)
        return existing.to_dict()
            
    async def delete(self, list_id: int) -> bool:
        query = select(BuyListsEntity).where(BuyListsEntity.id == list_id)
        result = await self.session.execute(query)
        chassis = result.scalars().first()
        
        if not chassis:
            return False
            
        await self.session.delete(chassis)
        await self.session.commit()
        return True
    
    async def search(
        self,
        list_type: Optional[str] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None
    ) -> List[BuyListsEntity]:
        query = select(BuyListsEntity)

        filters = {
            'type': (BuyListsEntity.type.ilike, f"%{list_type}%"),
            'min_price': (BuyListsEntity.total_price >= min_price),
            'max_price': (BuyListsEntity.total_price <= max_price),
            'date_from': (BuyListsEntity.datetime_create >= date_from),
            'date_to': (BuyListsEntity.datetime_create <= date_to)
        }

        for param, (condition, value) in filters.items():
            if value is not None:
                query = query.where(condition(value))

        result = await self.session.execute(query)
        buy_lists = result.scalars().all()
        return [buy_list.to_dict() for buy_list in buy_lists]
    
    async def delete_product(self, buy_list_id: int, product_index: int) -> bool:
        query = select(BuyListsEntity).where(BuyListsEntity.id == buy_list_id)
        result = await self.session.execute(query)
        buy_list = result.scalars().first()
        
        if not buy_list:
            return False
        
        # Проверяем, что индекс находится в допустимых пределах
        if product_index < 0 or product_index >= len(buy_list.products):
            return False
        
        # Создаем копию списка, чтобы SQLAlchemy отследил изменения
        products = list(buy_list.products)
        
        # Удаляем продукт по индексу
        products.pop(product_index)
        
        # Присваиваем измененный список обратно
        buy_list.products = products
        
        # Явно помечаем объект как измененный
        from sqlalchemy.orm import attributes
        attributes.flag_modified(buy_list, "products")
        
        await self.session.commit()
        return True