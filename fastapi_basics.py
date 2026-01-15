from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return (12,45,67)

@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id":item_id}