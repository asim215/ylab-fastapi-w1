from typing import Optional

from uuid import uuid4, UUID
from pydantic import BaseModel


# Shared properties
class SubmenuBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class SubmenuCreate(SubmenuBase):
    id: UUID = uuid4()
    title: str
    # description: str
    description: Optional[str]


# Properties to receive on item update
class SubmenuUpdate(SubmenuBase):
    title: str
    # description: str
    description: Optional[str]


# Properties shared by models stored in DB
class SubmenuInDBBase(SubmenuBase):
    id: UUID
    title: str
    description: str
    dishes_count: int

    class Config:
        orm_mode = True


# Properties to return to client
class Submenu(SubmenuInDBBase):
    id: UUID
    title: str
    description: str
    dishes_count: int


# Properties properties stored in DB
class SubmenuInDB(SubmenuInDBBase):
    pass
