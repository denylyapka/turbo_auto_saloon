from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db

from app.services.test_services.detail import DetailService, BrandService, CategoryService, ReviewService, CrossReferenceService, CompatibilityService

from app.models.dtoModels.ReviewDTO import ReviewDTO, ReviewEditModeDTO

from app.models.dbModels.Details.Entities.ReviewEntity import ReviewEntity


router = APIRouter()


@router.get("/detail")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    repo = DetailService(session)
    data = await DetailService.get_all(self=repo)
    return data

@router.get("/detail/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DetailService(session)
    data = await DetailService.get_by_id(self=repo, detail_id=id)
    return data

@router.get("/detail/part_number/{part_number}")
async def get_by_part_number(part_number: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DetailService(session)
    data = await DetailService.get_by_part_number(self=repo, part_number=part_number)
    return data

@router.get("/detail/oem_number/{oem_number}")
async def get_by_oem_number(oem_number: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DetailService(session)
    data = await DetailService.get_by_oem_number(self=repo, oem_number=oem_number)
    return data

@router.get("/detail/brand/{brand_id}")
async def get_by_brand(brand_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DetailService(session)
    data = await DetailService.get_by_brand(self=repo, brand_id=brand_id)
    return data

@router.get("/detail/category/{category_id}")
async def get_by_category(category_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DetailService(session)
    data = await DetailService.get_by_category(self=repo, category_id=category_id)
    return data



# BRANDS

@router.get("/brands")
async def get_all_brands(session: AsyncSession = Depends(fastapi_get_db)):
    repo = BrandService(session)
    data = await BrandService.get_all(self=repo)
    return data

@router.get("/brands/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = BrandService(session)
    data = await BrandService.get_by_id(self=repo, brand_id=id)
    return data

@router.get("/brands/name/{name}")
async def get_by_name(name: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = BrandService(session)
    data = await BrandService.get_by_name(self=repo, name=name)
    return data


# CATEGORIES

@router.get("/categories")
async def get_all_categories(session: AsyncSession = Depends(fastapi_get_db)):
    repo = CategoryService(session)
    data = await CategoryService.get_all(self=repo)
    return data

@router.get("/categories/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CategoryService(session)
    data = await CategoryService.get_by_id(self=repo, category_id=id)
    return data

@router.get("/categories/name/{name}")
async def get_by_name(name: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CategoryService(session)
    data = await CategoryService.get_by_name(self=repo, name=name)
    return data


# CROSS REFERENCES

@router.get("/cross_references")
async def get_all_cross_references(session: AsyncSession = Depends(fastapi_get_db)):
    repo = CrossReferenceService(session)
    data = await CrossReferenceService.get_all(self=repo)
    return data

@router.get("/cross_references/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CrossReferenceService(session)
    data = await CrossReferenceService.get_by_id(self=repo, cross_ref_id=id)
    return data

@router.get("/cross_references/part_id/{part_number}")
async def get_by_part_id(part_number: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CrossReferenceService(session)
    data = await CrossReferenceService.get_by_part_id(self=repo, part_number=part_number)
    return data

@router.get("/cross_references/brand_and_number/{brand}/{number}")
async def get_by_brand_and_number(brand: str, number: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CrossReferenceService(session)
    data = await CrossReferenceService.get_by_brand_and_number(self=repo, brand=brand, number=number)
    return data


# COMPATIBILITY

@router.get("/compatibilities")
async def get_all_compatibilities(session: AsyncSession = Depends(fastapi_get_db)):
    repo = CompatibilityService(session)
    data = await CompatibilityService.get_all(self=repo)
    return data

@router.get("/compatibilities/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CompatibilityService(session)
    data = await CompatibilityService.get_by_id(self=repo, compatibility_id=id)
    return data
