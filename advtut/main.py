from pydantic import BaseModel
from kink import di
from .bootstrap import bootstrap

from fastapi import FastAPI
from typing import Union

bootstrap()
from .models.user import User

app = FastAPI()


class NovoUserInput(BaseModel):
    name: str = None
    email: str = None


@app.get("/")
async def index():
    return di["config"]


@app.post("/user")
async def new_user(dados: NovoUserInput):
    user = User()
    user.name = dados.name
    user.email = dados.email
    user.save()

    return "ok"


@app.get("/user")
async def list_users():

    users = User.all()


    return users.serialize()



@app.get("/user/{user_id}")
async def find_user(user_id):

    user = User.find(user_id)

    return user.serialize()

@app.put("/user/{user_id}")
async def find_user(user_id, dados: NovoUserInput):

    user = User.find(user_id)

    user.name = dados.name 
    user.email = dados.email 

    user.save()

    return user.serialize()


@app.delete("/user/{user_id}")
async def delete_user(user_id):

    user = User.find(user_id)
    user.delete()

    return "Deletado"

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    print("item_id: ", item_id)
    return {"item_id": item_id, "q": q}
