from fastapi import APIRouter


router = APIRouter()


@router.get("/", response_model=List[schemas.Menu])
def read_menus(
    pass
