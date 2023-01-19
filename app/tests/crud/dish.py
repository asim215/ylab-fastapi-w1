from app.schemas.dish import DishCreate

req_json = {
    "title": "My dish 1",
    "description": "My dish description 1",
    "price": "12.50",
}

dish = DishCreate(**req_json)
print(dish)

# resp_json = {
#     "id": "602033b3-0462-4de1-a2f8-d8494795e0c0",
#     "title": "My dish 1",
#     "description": "My dish description 1",
#     "price": "12.50"
# }
