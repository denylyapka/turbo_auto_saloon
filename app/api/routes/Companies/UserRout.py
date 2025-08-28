from fastapi import APIRouter, HTTPException
from app.models.dtoModels.Companies.CompanyDto import CompanyCreate, CompanyRead
from app.services.test_services.company import CompanyCrud

router = APIRouter()


@router.post("/", response_model=CompanyRead)
async def create_company(company: CompanyCreate):
    created = CompanyCrud.create_company(company)
    if not created:
        raise HTTPException(status_code=400, detail="Cannot create company")
    return created


@router.get("/{company_id}", response_model=CompanyRead)
async def get_company(company_id: int):
    company = CompanyCrud.get_company(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
