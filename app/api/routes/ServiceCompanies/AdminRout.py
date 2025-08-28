from fastapi import APIRouter, HTTPException
from app.models.dtoModels.ServiceCompanies.ServiceCompanyDto import ServiceCompanyCreate, ServiceCompanyRead
from app.services.test_services.service_companies import ServiceCompanyCrud

router = APIRouter()


@router.put("/{relation_id}", response_model=ServiceCompanyRead)
async def update_relation(relation_id: int, data: ServiceCompanyCreate):
    updated = ServiceCompanyCrud.update_relation(relation_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Relation not found")
    return updated


@router.delete("/{relation_id}", response_model=dict)
async def delete_relation(relation_id: int):
    deleted = ServiceCompanyCrud.delete_relation(relation_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Relation not found")
    return {"status": "deleted"}
