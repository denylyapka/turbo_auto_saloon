from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db

from app.models.dtoModels.CarTotalDTO import CarFiltersDTO
from app.services.test_services.car import CarEntityService, EngineService, ChassisService, InteriorService, DimensionsService

router = APIRouter()


@router.get("/car_entity")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    repo = CarEntityService(session)
    data = await CarEntityService.get_all(self=repo)
    return data

@router.get("/car_entity/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CarEntityService(session)
    data = await CarEntityService.get_by_id(self=repo, car_id=id)
    return data

@router.get("/car_entity/vin/{vin}")
async def get_by_vin(vin: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CarEntityService(session)
    data = await CarEntityService.get_by_vin(self=repo, vin=vin)
    return data

@router.post("/car_entity/filters")
async def get_by_filters(filters: CarFiltersDTO, session: AsyncSession = Depends(fastapi_get_db)):
    print(111)
    repo = CarEntityService(session)
    data = await CarEntityService.get_by_filters(self=repo, filters=filters)
    return data


@router.get("/engine/{id}")
async def get_engine_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = EngineService(session)
    data = await EngineService.get_by_id(self=repo, engine_id=id)
    return data

@router.get("/engine")
async def get_all_engines(session: AsyncSession = Depends(fastapi_get_db)):
    repo = EngineService(session)
    data = await EngineService.get_all(self=repo)
    return data


@router.get("/chassis/{id}")
async def get_chassis_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ChassisService(session)
    data = await ChassisService.get_by_id(self=repo, chassis_id=id)
    return data

@router.get("/chassis")
async def get_all_chassis(session: AsyncSession = Depends(fastapi_get_db)):
    repo = ChassisService(session)
    data = await ChassisService.get_all(self=repo)
    return data


@router.get("/interior/{id}")
async def get_interior_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = InteriorService(session)
    data = await InteriorService.get_by_id(self=repo, interior_id=id)
    return data

@router.get("/interior")
async def get_all_interior(session: AsyncSession = Depends(fastapi_get_db)):
    repo = InteriorService(session)
    data = await InteriorService.get_all(self=repo)
    return data


@router.get("/dimensions/{id}")
async def get_dimensions_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DimensionsService(session)
    data = await DimensionsService.get_by_id(self=repo, dimensions_id=id)
    return data

@router.get("/dimensions")
async def get_all_dimensions(session: AsyncSession = Depends(fastapi_get_db)):
    repo = DimensionsService(session)
    data = await DimensionsService.get_all(self=repo)
    return data
