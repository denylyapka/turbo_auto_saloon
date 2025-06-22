from datetime import datetime
from pydantic import BaseModel
from typing import List, Dict, Optional

from app.models.dtoModels.Entity import Entity


class FinesDTO(Entity):   
    id: int
    name_fine: str
    description: str | None = None
    price: int
    deadline_pay: datetime
    datetime_receipt: datetime
