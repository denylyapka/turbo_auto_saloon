from fastapi import APIRouter

from app.api.routes.User.UserRout import router as user_user_rout
from app.api.routes.User.AdminRout import router as admin_user_rout
from app.api.routes.BuyListsRout import router as bl_rout
from app.api.routes.FinesRout import router as fines_rout

api_router = APIRouter()

api_router.include_router(user_user_rout, prefix="/user", tags=["User"])
api_router.include_router(admin_user_rout, prefix="/user/admin", tags=["[ADMIN] User"])

api_router.include_router(bl_rout, prefix="/buy_list", tags=["Buy List"])
api_router.include_router(fines_rout, prefix="/fines_rout", tags=["Fines"])
