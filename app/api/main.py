from fastapi import APIRouter

from app.api.routes.Services.UserRout import router as services_user_router

from app.api.routes.Companies.UserRout import router as companies_user_router

from app.api.routes.Categories.UserRout import router as categories_user_router

from app.api.routes.ServiceCompanies.UserRout import router as service_companies_user_router

from app.api.routes.CategoryHierarchies.UserRout import router as category_hierarchies_user_router

api_router = APIRouter()

api_router.include_router(services_user_router,
                          prefix="/services", tags=["services"])

api_router.include_router(companies_user_router,
                          prefix="/companies", tags=["companies"])

api_router.include_router(categories_user_router,
                          prefix="/categories", tags=["categories"])

api_router.include_router(service_companies_user_router,
                          prefix="/service_companies", tags=["service_companies"])

api_router.include_router(category_hierarchies_user_router,
                          prefix="/category_hierarchies", tags=["category_hierarchies"])
