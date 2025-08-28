from pydantic import BaseModel


class CategoryHierarchyBase(BaseModel):
    parent_category: int
    child_category: int


class CategoryHierarchyCreate(CategoryHierarchyBase):
    pass


class CategoryHierarchy(CategoryHierarchyBase):
    id: int

    class Config:
        from_attributes = True
