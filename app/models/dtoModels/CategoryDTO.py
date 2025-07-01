from pydantic import BaseModel
from typing import Optional


class CategoryDTO(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None
