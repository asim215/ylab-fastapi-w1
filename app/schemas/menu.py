from typing import Optional

from pydantic import BaseModel
from uuid import uuid4, UUID


# Shared properties
class MenuBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class MenuCreate(MenuBase):
    id: UUID = uuid4()
    title: str
    # description: str
    description: Optional[str]


# Properties to receive on item update
class MenuUpdate(MenuBase):
    title: str
    # description: str
    description: Optional[str]


# Properties shared by models stored in DB
class MenuInDBBase(MenuBase):
    # Convert to UUID from str request
    id: UUID
    title: str
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class Menu(MenuInDBBase):
    id: UUID
    title: str
    description: str
    submenus_count: int
    dishes_count: int


# Properties properties stored in DB
class MenuInDB(MenuInDBBase):
    pass
