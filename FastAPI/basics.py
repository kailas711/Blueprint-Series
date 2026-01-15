from unittest.mock import Base
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return (12,45,67)

@app.get("/item/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short:bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": 'This is an amazing item that has long description'}
        )
    return item


# Request Boody 
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str 
    description: str | None = None 
    price: float 
    tax: float | None = None 


@app.post("/create_item")
async def create_items(item: Item):
    item_dict = item.model_dump()
    print(item_dict)
    if item_dict['name'] == 'kailas':
        item_dict.update({"description":"Root access granted"})
    return item_dict