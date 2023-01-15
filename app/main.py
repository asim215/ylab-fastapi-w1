from fastapi import FastAPI
import uvicorn

from app.api.v1.api import api_router
from app.core.config import settings
from router1 import router_r1

app = FastAPI(title="YLab-W1")

app.include_router(router_r1)
# app.include_router(api_router)
app.include_router(api_router, prefix=settings.API_V1_STR)
# api.add_api_route("v1/routers/menus")

# @api.get("/api/v1/menus")
# def menus():
#     """Return menus"""
#     return [
#         {
#             "id": "a2eb416c-2245-4526-bb4b-6343d5c5016f",
#             "title": "My menu 1",
#             "description": "My menu description 1",
#             "submenus_count": 0,
#             "dishes_count": 0,
#         }
#     ]


@app.get("/")
async def index() -> dict:
    return {"message": "Hello Home page"}


# uvicorn.run(app)
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
