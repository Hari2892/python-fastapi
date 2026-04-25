from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Hari, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}