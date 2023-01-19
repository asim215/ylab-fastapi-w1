from typing import List, Dict
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import schemas
from app.models.menu import Menu
from app.schemas import MenuCreate, MenuUpdate
from app.models.submenu import Submenu
from app.db.session import factory
from app.crud.crud_menu import CRUDMenu
from uuid import UUID

router = APIRouter()


@router.post("/")
async def add_menu(req: MenuCreate):
    async with factory() as sess:
        async with sess.begin():
            crud = CRUDMenu(sess)
            menu = Menu(
                id=req.id,
                title=req.title,
                description=req.description,
            )
            return await crud.insert(menu)


@router.patch("/")
async def update_menu(id: UUID, req: MenuUpdate):
    async with factory() as sess:
        async with sess.begin():
            crud = CRUDMenu(sess)
            menu_dict = req.dict(exclude_unset=True)
            return await crud.update(id, menu_dict)


@router.delete("/{id}")
async def delete_menu(id: UUID):
    async with factory() as sess:
        async with sess.begin():
            crud = CRUDMenu(sess)
            return await crud.delete(id)


@router.get("/")
async def get_menus():
    async with factory() as sess:
        async with sess.begin():
            crud = CRUDMenu(sess)
            return await crud.get_all()


@router.get("/{id}")
async def get_menu(id: UUID):
    async with factory() as sess:
        async with sess.begin():
            curd = CRUDMenu(sess)
            return await curd.get(id)


# def sess_db():
#     db = factory()
#     try:
#         yield db
#     finally:
#         db.close()


# Request validation by pydantic from schema base class
# @router.post("/")
# async def add_menu(req: MenuCreate, sess: Session = Depends(sess_db)):
#     print("Inside post menu")
#     crud: CRUDMenu = CRUDMenu(sess)
#     print("Create instance of menu from req")
#     menu: Menu = Menu(title=req.title, description=req.description)
#     result = crud.insert(menu)
#     return await JSONResponse(content={"message": "menu created"}, status_code=200)
#     if result is True:
#         return menu
#     else:
#         return JSONResponse(
#             content={"message": "create menu problem encountered"}, status_code=500
#         )


# @router.get("/", response_model=List[schemas.Menu])
# # def get(sess: Session = Depends(sess_db)):
# async def get_all_menus(sess: Session = Depends(sess_db)):
#     """Return menus"""
#     crud: CRUDMenu = CRUDMenu(sess)
#     result = crud.get_all()
#     return result
#     # return JSONResponse(content=result)
#     # return [
#     #     {
#     #         "id": "a2eb416c-2245-4526-bb4b-6343d5c5016f",
#     #         "title": "My menu 1",
#     #         "description": "My menu description 1",
#     #         "submenus_count": 0,
#     #         "dishes_count": 0,
#     #     }
#     # ]


# # @router.get("/t", response_model=Dict[str, str])
# @router.get("/t")
# async def get_t(sess: Session = Depends(sess_db)):
#     return JSONResponse(content={"message": "test results"}, status_code=200)


# # def get_menu():
# #     pass


# @router.get("/{id}", response_model=schemas.Menu)
# def get_menu(id: int, sess: Session = Depends(sess_db)):
#     crud: CRUDMenu = CRUDMenu(sess)
#     result = crud.get(id)
#     return result
