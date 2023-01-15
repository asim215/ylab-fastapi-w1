from fastapi import APIRouter


router = APIRouter()


@router.get("/", response_model=List[schemas.Dish])
def read_dishes(
    pass
