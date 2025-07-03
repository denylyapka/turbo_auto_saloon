from fastapi import APIRouter

from app.api.routes.User.UserRout import router as user_user_rout
from app.api.routes.User.AdminRout import router as admin_user_rout

from app.api.routes.WatchList.UserRout import router as user_watch_list_rout
from app.api.routes.WatchList.AdminRout import router as admin_watch_list_rout

from app.api.routes.BuyList.UserRout import router as user_buy_list_rout

from app.api.routes.Car.UserRout import router as user_car_rout
from app.api.routes.Car.AdminRout import router as admin_car_rout


api_router = APIRouter()

api_router.include_router(user_user_rout, prefix="/user", tags=["User"])
api_router.include_router(admin_user_rout, prefix="/user/admin", tags=["[ADMIN] User"])

api_router.include_router(user_watch_list_rout, prefix="/watch_list", tags=["Watch List"])
api_router.include_router(admin_watch_list_rout, prefix="/watch_list/admin", tags=["[ADMIN] Watch List"])

api_router.include_router(user_buy_list_rout, prefix="/buy_list", tags=["Buy List"])

api_router.include_router(user_car_rout, prefix="/car", tags=["Car"])
api_router.include_router(admin_car_rout, prefix="/car/admin", tags=["[ADMIN] Car"])
