from typing import Optional

from uuid import UUID
from pydantic import BaseModel


# Shared properties
class SubmenuBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class SubmenuCreate(SubmenuBase):
    title: str
    description: str


# Properties to receive on item update
class SubmenuUpdate(SubmenuBase):
    title: str
    description: str


# Properties shared by models stored in DB
class SubmenuInDBBase(SubmenuBase):
    id: UUID
    # id: int
    title: str
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class Submenu(SubmenuInDBBase):
    id: UUID
    # id: int
    title: str
    description: str


# Properties properties stored in DB
class SubmenuInDB(SubmenuInDBBase):
    pass
