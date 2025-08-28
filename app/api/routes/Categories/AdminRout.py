from fastapi import APIRouter, HTTPException
from app.models.dtoModels.Categories.CategoryDto import CategoryCreate, CategoryRead
from app.services.test_services.category import CategoryCrud

router = APIRouter()


@router.put("/{category_id}", response_model=CategoryRead)
async def update_category(category_id: int, category: CategoryCreate):
    updated = CategoryCrud.update_category(category_id, category)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated


@router.delete("/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    deleted = CategoryCrud.delete_category(category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"status": "deleted"}
