from fastapi import APIRouter


router = APIRouter()


@router.get("/", response_model=List[schemas.Submenu])
def read_submenus(
    pass
