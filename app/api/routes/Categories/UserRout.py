from fastapi import APIRouter, HTTPException
from app.models.dtoModels.Categories.CategoryDto import CategoryCreate, CategoryRead
from app.services.test_services.category import CategoryCrud

router = APIRouter()


@router.post("/", response_model=CategoryRead)
async def create_category(category: CategoryCreate):
    created = CategoryCrud.create_category(category)
    if not created:
        raise HTTPException(status_code=400, detail="Cannot create category")
    return created


@router.get("/{category_id}", response_model=CategoryRead)
async def get_category(category_id: int):
    category = CategoryCrud.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
