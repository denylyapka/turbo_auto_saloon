from pydantic import BaseModel
from typing import Optional
from app.models.dtoModels.Entity import Entity

class UserBuyListsDTO(Entity):
    id: int
    user_id: int
    buy_list_id: int
    