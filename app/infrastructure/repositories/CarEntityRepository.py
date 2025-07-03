from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarEntity import CarEntity
from app.models.dbModels.Cars.IRepositories.ICarEntityRepository import ICarRepository

from sqlalchemy.sql.operators import eq, gt, lt, like_op, ge, le, in_op
from sqlalchemy.exc import SQLAlchemyError

from app.models.dtoModels.CarTotalDTO import CarFiltersDTO


class CarRepository(ICarRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, car: CarEntity) -> CarEntity:
        self.session.add(car)
        await self.session.commit()
        await self.session.refresh(car)
        return car
    
    async def get_by_id(self, car_id: int) -> Optional[CarEntity]:
        query = select(CarEntity).where(CarEntity.id == car_id)
        result = await self.session.execute(query)
        car = result.scalars().first()
        return car.to_dict() if car else None
    
    async def get_all(self) -> List[CarEntity]:
        query = select(CarEntity)
        result = await self.session.execute(query)
        cars = result.scalars().all()
        return [car.to_dict() for car in cars] if cars else []
    
    async def get_by_vin(self, vin: str) -> Optional[CarEntity]:
        query = select(CarEntity).where(CarEntity.vin_id == vin)
        result = await self.session.execute(query)
        car = result.scalars().first()
        return car.to_dict() if car else None
            
    async def update(self, car_id: int, car_data: CarEntity) -> Optional[dict]:
        """Обновить данные автомобиля"""
        print(f"4. Calling update with car_id={car_id} Должно быть 2")  # Должно быть 2

        query = select(CarEntity).where(CarEntity.id == car_id)
        print(f"5. Calling update with car_id={car_id} Должно быть 2")  # Должно быть 2
        result = await self.session.execute(query)
        car = result.scalars().first()

        print("car:", car)
        
        if not car:
            raise HTTPException(status_code=404, detail=f"ВАТАФАК car id={car_id}")
            
        # Обновляем только существующие атрибуты с проверкой на None
        for field in vars(car_data):
            if not field.startswith('_') and hasattr(car, field):
                value = getattr(car_data, field)
                if value is not None:
                    setattr(car, field, value)
        
        self.session.add(car)
        await self.session.commit()
        await self.session.refresh(car)
        
        return car.to_dict() if car else None
    
    async def delete(self, car_id: int) -> bool:
        query = select(CarEntity).where(CarEntity.id == car_id)
        result = await self.session.execute(query)
        car = result.scalars().first()
        
        if not car:
            return False
            
        await self.session.delete(car)
        await self.session.commit()
        return True
    
    async def get_by_filters(self, filters: CarFiltersDTO) -> list[CarEntity]:
        operator_mapping = {
            "eq": eq,
            "gt": gt,
            "lt": lt,
            "ge": ge,
            "le": le,
            "like": like_op,
            "in": in_op,
        }

        conditions = []
        
        for filter in filters.filters:
            try:
                # Проверяем существование поля
                if not hasattr(CarEntity, filter.field):
                    raise AttributeError(f"Field '{filter.field}' doesn't exist in CarEntity")
                
                column = getattr(CarEntity, filter.field)
                
                operator_func = operator_mapping.get(filter.operator)
                if not operator_func:
                    raise ValueError(f"Unknown operator: '{filter.operator}'")
                
                value = filter.value.split(",") if filter.operator == "in" else filter.value
                
                conditions.append(operator_func(column, value))
            
            except (AttributeError, ValueError) as e:
                # Логируем ошибку и пропускаем невалидный фильтр
                print(f"Invalid filter skipped: {e}")
                continue
        
        try:
            query = select(CarEntity)
            if conditions:
                query = query.where(and_(*conditions))
            
            result = await self.session.execute(query)
            cars = result.scalars().all()
            return [car.to_dict() for car in cars] if cars else []
        
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            return []
        