from app.schemas.submenu import SubmenuCreate

req_json = {"title": "My submenu 1", "description": "My submenu description 1"}

submenu = SubmenuCreate(**req_json)
print(submenu)

# resp_json = {
#     "id": "bc19488a-cc0e-4eaa-8d21-4d486a45392f",
#     "title": "My submenu 1",
#     "description": "My submenu description 1",
#     "dishes_count": 0
# }
