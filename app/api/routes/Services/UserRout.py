from fastapi import APIRouter, HTTPException
from app.models.dtoModels.Services.ServiceDto import ServiceCreate, ServiceRead
from app.services.test_services.service import ServiceCrud

router = APIRouter()


@router.post("/", response_model=ServiceRead)
async def create_service(service: ServiceCreate):
    created = ServiceCrud.create_service(service)
    if not created:
        raise HTTPException(status_code=400, detail="Cannot create service")
    return created


@router.get("/{service_id}", response_model=ServiceRead)
async def get_service(service_id: int):
    service = ServiceCrud.get_service(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
