from fastapi import APIRouter, HTTPException
from app.models.dtoModels.Companies.CompanyDto import CompanyCreate, CompanyRead
from app.services.test_services.company import CompanyCrud

router = APIRouter()


@router.put("/{company_id}", response_model=CompanyRead)
async def update_company(company_id: int, company: CompanyCreate):
    updated = CompanyCrud.update_company(company_id, company)
    if not updated:
        raise HTTPException(status_code=404, detail="Company not found")
    return updated


@router.delete("/{company_id}", response_model=dict)
async def delete_company(company_id: int):
    deleted = CompanyCrud.delete_company(company_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"status": "deleted"}
