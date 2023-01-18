from typing import Optional

from pydantic import BaseModel


# Shared properties
class DishBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


# Properties to receive on item creation
class DishCreate(DishBase):
    title: str
    description: str
    price: float


# Properties to receive on item update
class DishUpdate(DishBase):
    title: str
    description: str
    price: float


# Properties shared by models stored in DB
class DishInDBBase(DishBase):
    id: int
    # id: str
    title: str
    description: str
    price: float
    # price: str

    class Config:
        orm_mode = True


# Properties to return to client
class Dish(DishInDBBase):
    id: int
    # id: str
    title: str
    description: str
    price: float
    # price: str


# Properties properties stored in DB
class DishInDB(DishInDBBase):
    pass
