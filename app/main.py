from fastapi import FastAPI
import uvicorn

# from v1.routers import menus

app = FastAPI()

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
def index():
    return "Hello"


uvicorn.run(app)
