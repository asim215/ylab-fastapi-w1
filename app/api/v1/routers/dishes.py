from typing import List
from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Dish])
def read_dishes():
    return [
        {
            "id": "602033b3-0462-4de1-a2f8-d8494795e0c0",
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": "12.50",
        }
    ]
