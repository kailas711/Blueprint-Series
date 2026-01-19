from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# # Enum definition 
class ModelName(str, Enum): # predefining values that param model_name can have
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# Declaring a fixed path parameter
@app.get("Path_params/users/me") # Order of execution , first /me then .user_id
async def read_user_me():
    return {"user_id": "the current user"}

# Declaring a dynamic path parameter
@app.get("Path_params/users/{user_id}")
async def read_user(user_id: str): # Type hints added for data validaiton
    return {"user_id": user_id} # The return type can be converted to int, eventhough we pass it as string

# Exampele of getting using predefined values ( ENUM )
@app.get("Path_params/models/{model_name}")
async def get_model(model_name: ModelName): # model_name is assigned Enum Type
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


### Query Parameters 
# Multiple path and query parameter in same URL
@app.get("Query_params/users/{user_id}/items/{item_id}") 
async def read_user_item(
    user_id: int, item_id: str, needy: str, # Required query parameter
    q: str | None = None, # Optional query parameter
    short: bool = False # Auto Type conversion from String to Bool
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item