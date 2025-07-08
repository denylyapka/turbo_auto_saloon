from pydantic import BaseModel


class CrossReferenceDTO(BaseModel):
    part_id: int
    brand: str
    number: str
