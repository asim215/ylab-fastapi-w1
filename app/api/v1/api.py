from fastapi import APIRouter

from app.api.v1.routers import menus, submenus, dishes

api_router = APIRouter()
api_router.include_router(menus.router, prefix="/menus", tags=["menus"])
