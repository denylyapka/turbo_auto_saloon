from fastapi import APIRouter, HTTPException
from app.models.dtoModels.CategoryHierarchies.CategoryHierarchyDto import CategoryHierarchyCreate, CategoryHierarchyRead
from app.services.test_services.category_hierarchies import CategoryHierarchyCrud

router = APIRouter()


@router.post("/", response_model=CategoryHierarchyRead)
async def create_hierarchy(data: CategoryHierarchyCreate):
    created = CategoryHierarchyCrud.create_hierarchy(data)
    if not created:
        raise HTTPException(status_code=400, detail="Cannot create hierarchy")
    return created


@router.get("/{hierarchy_id}", response_model=CategoryHierarchyRead)
async def get_hierarchy(hierarchy_id: int):
    hierarchy = CategoryHierarchyCrud.get_hierarchy(hierarchy_id)
    if not hierarchy:
        raise HTTPException(status_code=404, detail="Hierarchy not found")
    return hierarchy
