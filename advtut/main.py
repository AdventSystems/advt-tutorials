from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
async def index():
    return "oi mundo"


@app.get("/hellow")
async def index2():
    return "Hi hellow"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    print("item_id: ", item_id)
    return {"item_id": item_id, "q": q}
