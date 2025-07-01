from pydantic import BaseModel


class CrossReferenceDTO(BaseModel):
    id: int
    part_id: int
    brand: str
    number: str
