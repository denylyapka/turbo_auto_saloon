from fastapi import APIRouter, HTTPException
from app.models.dtoModels.ServiceCompanies.ServiceCompanyDto import ServiceCompanyCreate, ServiceCompanyRead
from app.services.test_services.service_companies import ServiceCompanyCrud

router = APIRouter()


@router.post("/", response_model=ServiceCompanyRead)
async def create_relation(data: ServiceCompanyCreate):
    created = ServiceCompanyCrud.create_relation(data)
    if not created:
        raise HTTPException(status_code=400, detail="Cannot create relation")
    return created


@router.get("/{relation_id}", response_model=ServiceCompanyRead)
async def get_relation(relation_id: int):
    relation = ServiceCompanyCrud.get_relation(relation_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relation not found")
    return relation
