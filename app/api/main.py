from fastapi import APIRouter

from app.api.routes.UserRout import router as user_rout

api_router = APIRouter()

api_router.include_router(user_rout, prefix="/user", tags=["user"])
