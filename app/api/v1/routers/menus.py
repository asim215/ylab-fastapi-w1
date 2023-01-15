from typing import List
from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Menu])
def read_menus():
    """Return menus"""
    return [
        {
            "id": "a2eb416c-2245-4526-bb4b-6343d5c5016f",
            "title": "My menu 1",
            "description": "My menu description 1",
            "submenus_count": 0,
            "dishes_count": 0,
        }
    ]
