import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.FinesRepository import FinesRepository
from app.models.dbModels.Fines.FinesEntity import FinesEntity as Fines


async def get_fine_by_id(fine_id: int, session: AsyncSession) -> Fines:
    repo_fines = FinesRepository(session)
    return await repo_fines.get_by_id(fine_id=fine_id)

async def get_all_fines(session: AsyncSession) -> Any:
    repo_fines = FinesRepository(session)
    return await repo_fines.get_all()

async def create_fine(session: AsyncSession) -> Any:
    repo_fines = FinesRepository(session)

    fine = Fines(
        name_fine="name_fine",
        description="description",
        price=100,
        deadline_pay=datetime.datetime.now(),
        datetime_receipt=datetime.datetime.now()
    )

    return await repo_fines.create(fine=fine)
