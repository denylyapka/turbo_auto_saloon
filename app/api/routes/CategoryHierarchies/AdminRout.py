from fastapi import APIRouter, HTTPException
from app.models.dtoModels.CategoryHierarchies.CategoryHierarchyDto import CategoryHierarchyCreate, CategoryHierarchyRead
from app.services.test_services.category_hierarchies import CategoryHierarchyCrud

router = APIRouter()


@router.put("/{hierarchy_id}", response_model=CategoryHierarchyRead)
async def update_hierarchy(hierarchy_id: int, data: CategoryHierarchyCreate):
    updated = CategoryHierarchyCrud.update_hierarchy(hierarchy_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Hierarchy not found")
    return updated


@router.delete("/{hierarchy_id}", response_model=dict)
async def delete_hierarchy(hierarchy_id: int):
    deleted = CategoryHierarchyCrud.delete_hierarchy(hierarchy_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Hierarchy not found")
    return {"status": "deleted"}
