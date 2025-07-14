from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.discounts import DiscountService

router = APIRouter()


@router.get("/")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.get_all()
    return data

@router.get("/cars")
async def get_cars(session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.get_cars()
    return data

@router.get("/details")
async def get_details(session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.get_details()
    return data


@router.get("/car/{id}")
async def get_by_car_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.get_by_car_id(car_id=id)
    return data

@router.get("/detail/{id}")
async def get_by_detail_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.get_by_detail_id(detail_id=id)
    return data


@router.get("/{percent}")
async def get_by_discount_percents(percent: float, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.get_by_discount_percents(discount=percent)
    return data