from typing import Optional

from pydantic import BaseModel


# Shared properties
class MenuBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class MenuCreate(MenuBase):
    title: str
    description: str


# Properties to receive on item update
class MenuUpdate(MenuBase):
    title: str
    description: str


# Properties shared by models stored in DB
class MenuInDBBase(MenuBase):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class Menu(MenuInDBBase):
    id: int
    title: str
    description: str


# Properties properties stored in DB
class MenuInDB(MenuInDBBase):
    pass
