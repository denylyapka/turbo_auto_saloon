from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.user import (create_user, get_user_by_id, get_user_by_email, get_all, delete_user, update_user, get_hashed_password)

from app.models.dtoModels.UserDTO import UserDTO

from .utils.hash_password import hashing_password

router = APIRouter()


@router.get("/")
async def get_all_users(session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_all(session=session)
    return data