from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.discounts import DiscountService
from app.models.dtoModels.DiscountDTO import DiscountDTO

router = APIRouter()


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.get_by_id(discount_id=id)
    return data


@router.post("/")
async def create(discount: DiscountDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.create(discount=discount)
    return data


@router.delete("/{id}")
async def delete(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.delete(discount_id=id)
    return data


@router.put("/{id}")
async def update(id: int, discount: DiscountDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DiscountService(session)
    data = await repo.update(discount_id=id, discount=discount)
    return data