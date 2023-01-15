from typing import List
from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Submenu])
def read_submenus():
    return [
        {
            "id": "bc19488a-cc0e-4eaa-8d21-4d486a45392f",
            "title": "My submenu 1",
            "description": "My submenu description 1",
            "dishes_count": 0,
        }
    ]
