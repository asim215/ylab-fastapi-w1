from fastapi import APIRouter

from api.v1.routers import menus, submenus, dishes

# TODO Change prefixs
api_router = APIRouter()
api_router.include_router(menus.router, prefix="/menus", tags=["menus"])
api_router.include_router(submenus.router, prefix="/submenus", tags=["submenus"])
api_router.include_router(dishes.router, prefix="/dishes", tags=["dishes"])
