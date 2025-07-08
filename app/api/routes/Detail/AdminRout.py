from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db

from app.services.test_services.detail import DetailService, BrandService, ReviewService, CategoryService, CrossReferenceService, CompatibilityService

from app.models.dtoModels.DetailTotalDTO import DetailTotalDTO
from app.models.dtoModels.ReviewDTO import ReviewDTO, ReviewEditModeDTO
from app.models.dtoModels.CompatibilityDTO import CompatibilityDTO
from app.models.dtoModels.CrossReferenceDTO import CrossReferenceDTO

from app.models.dbModels.Details.Entities.BrandEntity import Brand
from app.models.dbModels.Details.Entities.CategoryEntity import Category
from app.models.dbModels.Details.Entities.ReviewEntity import ReviewEntity as Review
from app.models.dbModels.Details.Entities.CrossReferencesEntity import CrossReference
from app.models.dbModels.Details.Entities.CompatibilityEntity import Compatibility
from app.models.dbModels.Details.Entities.DetailEntity import DetailEntity


router = APIRouter()


# Заполнение бренды + категории + детали

@router.post("/detail")
async def create(details: DetailTotalDTO, session: AsyncSession = Depends(fastapi_get_db)):
    brand_data = Brand(
        name=details.name_brand,
        description=details.description,
        logo_url=details.logo_url
    )

    service_brand = BrandService(session)
    get_brand_id = await service_brand.get_by_name(name=details.name_brand)
    if get_brand_id:
        id_brand = get_brand_id["id"]

    response_brand_create = None
    if not get_brand_id:
        response_brand_create = await service_brand.create(brand=brand_data)
        id_brand = response_brand_create.id

    category_data = Category(
        name=details.name_category,
        parent_id=details.parent_id
    )
    
    service_category = CategoryService(session)  # Инициализация сервиса
    get_category_id = await service_category.get_by_name(name=details.name_category)
    if get_category_id:
        id_category = get_category_id["id"]
    
    response_category_create = None
    if not get_category_id:
        response_category_create = await service_category.create(category_data)
        id_category = response_category_create.id
    # return id_brand, get_brand_id, response_brand_create, response_category_create

    details_data = DetailEntity(
        name=details.name_detail,
        part_number=details.part_number,
        oem_number=details.oem_number,
        brand_id=id_brand,
        category_id=id_category,
        price=details.price,
        quantity=details.quantity,
        weight_kg=details.weight_kg,
        description=details.description,
        image_urls=details.image_urls,
        warranty_months=details.warranty_months,
        installation_guide_url=details.installation_guide_url,
        video_review_url=details.video_review_url
    )

    service_detail = DetailService(session)
    detail = await service_detail.create(detail=details_data)

    service_compatibility = CompatibilityService(session)
    compatibility_data = Compatibility(
        part_id=detail.id,
        make=details.make,
        model=details.model,
        year_from=details.year_from,
        year_to=details.year_to,
        engine_type=details.engine_type
    )
    compatibility = await service_compatibility.create(compatibility=compatibility_data)

    return {
        "detail": detail,
        "compatibility": compatibility
    }


# Удаление детали

@router.delete("/detail/{detail_id}")
async def delete(detail_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    service_detail = DetailService(session)
    detail_dict = await service_detail.get_by_id(detail_id=detail_id)

    if not detail_dict:
        raise HTTPException(status_code=404, detail="Detail not found")

    # Удаление совместимости
    service_compatibility = CompatibilityService(session)
    response_delete_compatibility = await service_compatibility.delete_by_detail_id(detail_id=detail_id)

    # Удаление кросс референсов
    service_cross_ref = CrossReferenceService(session)
    response_delete_cross_ref = await service_cross_ref.delete_by_part_id(part_id=detail_id)

    service_detail = DetailService(session)
    detail_delete_response = await service_detail.delete(detail_id=detail_id)

    return {
        "response_delete_compatibility": response_delete_compatibility,
        "response_delete_cross_ref": response_delete_cross_ref,
        "detail_delete_response": detail_delete_response
    }


# Удаление категории
@router.delete("/category/{category_id}")
async def delete_category(
    category_id: int,
    new_category_id: Optional[int] = None,
    session: AsyncSession = Depends(fastapi_get_db)
):
    service_category = CategoryService(session)
    category_dict = await service_category.get_by_id(category_id=category_id)

    if not category_dict:
        raise HTTPException(status_code=404, detail="Category not found")
    
    # Проверяем существование новой категории
    if new_category_id != None:
        if not await service_category.get_by_id(new_category_id):
            raise HTTPException(status_code=404, detail="New category not found")
        
    # Переносим детали в новую категорию
    await service_category.transfer_details(
        from_category_id=category_id,
        to_category_id=new_category_id
    )

    result = await service_category.delete(category_id)
    return {"deleted": result, "moved_to": new_category_id}


# Удаление бренда

@router.delete("/brand/{brand_id}")
async def delete_brand(
    brand_id: int,
    new_brand_id: Optional[int] = None,  # Необязательный параметр для переноса
    session: AsyncSession = Depends(fastapi_get_db)
):
    service_brand = BrandService(session)
    brand_dict = await service_brand.get_by_id(brand_id=brand_id)

    if not brand_dict:
        raise HTTPException(status_code=404, detail="Brand not found")
    
    # Проверяем существование новой категории
    if new_brand_id != None:
        if not await service_brand.get_by_id(new_brand_id):
            raise HTTPException(status_code=404, detail="New brand not found")
        
    # Переносим детали в новую категорию
    await service_brand.transfer_details(
        from_brand_id=brand_id,
        to_brand_id=new_brand_id,
    )

    result = await service_brand.delete(brand_id)
    return {"deleted": result, "moved_to": new_brand_id}


# REVIEW

@router.get("/reviews")
async def get_all_reviews(session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)
    data = await repo.get_all()
    return data

@router.get("/reviews/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)
    data = await repo.get_by_id(review_id=id)
    return data

@router.get("/reviews/part_number/{part_id}")
async def get_by_part_number(part_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)
    reviews = await repo.get_by_part_id(part_id=part_id)

    # Вычисляем средний рейтинг
    avg_rating = await repo.get_avg_rating(part_id=part_id)
    
    return {
        "reviews": reviews,
        "avg_rating": avg_rating
    }

@router.get("/reviews/user_id/{user_id}")
async def get_by_user_id(user_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)
    data = await repo.get_by_user_id(user_id=user_id)
    return data

@router.get("/reviews/rating_range/{min_rating}/{max_rating}")
async def get_by_rating_range(min_rating: int, max_rating: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)
    data = await repo.get_by_rating_range(min_rating=min_rating, max_rating=max_rating)
    return data


@router.post("/detail/review")
async def create_review(review: ReviewDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)

    review_data_check = Review(
        part_id=review.part_id,
        user_id=review.user_id
    )
    check_revies_by_uid_and_pid = await repo.check(review=review_data_check)
    if check_revies_by_uid_and_pid is True:
        return {
            "status": "error",
            "message": "Review already exists"}

    review_data = Review(
        part_id=review.part_id,
        user_id=review.user_id,
        rating=review.rating,
        comment=review.comment
    )
    response = await repo.create(review=review_data)
    return response

@router.delete("/detail/review/{review_id}")
async def delete_review(review_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)
    response = await repo.delete(review_id=review_id)
    return response

@router.put("/detail/review")
async def update_review(review: ReviewEditModeDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ReviewService(session)
    review_data = Review(
        id=review.id,
        part_id=review.part_id,
        user_id=review.user_id,
        rating=review.rating,
        comment=review.comment
    )
    response = await repo.update(review=review_data)
    return response



# COMPATIBILITY

@router.post("/detail/compatibility")
async def create_compatibility(compatibility: CompatibilityDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CompatibilityService(session)
    compatibility_data = Compatibility(
        part_id=compatibility.part_id,
        make=compatibility.make,
        model=compatibility.model,
        year_from=compatibility.year_from,
        year_to=compatibility.year_to,
        engine_type=compatibility.engine_type
    )
    response = await repo.create(compatibility=compatibility_data)
    return response

@router.delete("/detail/compatibility/{compatibility_id}")
async def delete_compatibility(compatibility_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CompatibilityService(session)
    response = await repo.delete(compatibility_id=compatibility_id)
    return response


# CROSS REFERENCES

@router.post("/detail/cross_reference")
async def create_cross_reference(cross_reference: CrossReferenceDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CrossReferenceService(session)
    cross_references_data = CrossReference(
        part_id=cross_reference.part_id,
        brand=cross_reference.brand,
        number=cross_reference.number
    )
    response = await repo.create(cross_ref=cross_references_data)
    return response

@router.delete("/detail/cross_reference/{cross_ref_id}")
async def delete_cross_reference(cross_ref_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CrossReferenceService(session)
    response = await repo.delete(cross_ref_id=cross_ref_id)
    return response

@router.delete("/detail/cross_reference/original/{part_id}")
async def delete_cross_reference_by_part_id(part_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CrossReferenceService(session)
    response = await repo.delete_by_part_id(part_id=part_id)
    return response