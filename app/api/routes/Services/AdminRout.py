from fastapi import APIRouter, HTTPException
from app.models.dtoModels.Services.ServiceDto import ServiceCreate, ServiceRead
from app.services.test_services.service import ServiceCrud

router = APIRouter()


@router.put("/{service_id}", response_model=ServiceRead)
async def update_service(service_id: int, service: ServiceCreate):
    updated = ServiceCrud.update_service(service_id, service)
    if not updated:
        raise HTTPException(status_code=404, detail="Service not found")
    return updated


@router.delete("/{service_id}", response_model=dict)
async def delete_service(service_id: int):
    deleted = ServiceCrud.delete_service(service_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"status": "deleted"}
