from app.schemas.menu import MenuCreate

json_req = {"title": "My menu 1", "description": "My menu description 1"}

menu = MenuCreate(**json_req)
print(menu)
