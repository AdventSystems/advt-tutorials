from pydantic import BaseModel
from pydantic import  ValidationError, validator
from kink import di
from .bootstrap import bootstrap

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Union

bootstrap()
from .models.user import User
from passlib.hash import pbkdf2_sha256
from passlib import pwd
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer, JwtRefreshBearer
app = FastAPI()


class NovoUserInput(BaseModel):
    name: str = None
    email: str = None
    password:str = None
    password2:str = None


    @validator('name')
    def mais_que_tres(cls, v):
        if len(v) < 3:
            raise ValueError('O nome tem que ter pelo menos 3 caracteres')
        return v.title()
    
    @validator("email")
    def validar_email(cls, v):
        if '@' not in v:
            raise ValueError("Email inválido.")
        return v


class LoginInput(BaseModel):
    email: str = None 
    password: str = None



    # @validator("password")
    # def validar_passowd(cls, v):
    #     if v != cls.password2:
    #         raise ValueError("Senhas diferentes")
    #     return v





@app.post("/user")
async def new_user(dados:NovoUserInput):

    if dados.password != dados.password2:
        return JSONResponse({
            "error":True,
            "data": "As senhas não são iguais"
        },422)
    
    obj = User()

    obj.name = dados.name  
    obj.email = dados.email 

    salt = pwd.genword(entropy=56, charset="ascii_62")

    obj.salt = salt


    hash = pbkdf2_sha256.hash(dados.password+":"+salt)    
     
    obj.hash = hash
    

    if obj.save():
        return JSONResponse({
            "error":False,
            "data": "Salvo com sucesso."
        }, 200)
    else:
        return JSONResponse({
            "error":True,
            "data": "Não foi possível salvar"
        }, 422)




@app.post("/user/login")
async def login(dados:LoginInput):

    user:User = User.where("email", dados.email).first()
    if user is None:
        return JSONResponse(
            {
                "error":True,
                "data":"Usuário não encontrado ou inválido",
            }, 404
        )
    salt = user.salt 

    if pbkdf2_sha256.verify(dados.password+":"+salt, user.hash):
        subject = {
            "user_id": user.id, 
            "name": user.name
            }
        
        return JSONResponse({
            "error":False,
            "data": {
                "access_token": di["access_security"].create_access_token(subject=subject),
                "refresh_token": di["refresh_security"].create_access_token(subject=subject)
            } 
        })
    return JSONResponse(
            {
                "error":True,
                "data":"Senha inválida.",
            }
        )




@app.get("/user/profile")
async def profile(credentials: JwtAuthorizationCredentials = di["security_access_token"]):

    if not credentials:
        return JSONResponse({
            "error":True,
            "data":"Sem aturoização"
        }, 401)
    
    user_id = credentials["user_id"]

    user = User.find(user_id)

    if user is None:
        return JSONResponse(
            {
                "error":True,
                "data":"Usuário não encontrado ou inválido",
            }, 404
        )
    
    

    return JSONResponse({
        "error":True,
        "data":user.serialize()
    }) 

# @app.post("/user")
# async def new_user(dados: NovoUserInput):
#     user = User()
#     user.name = dados.name
#     user.email = dados.email
#     user.save()

#     return "ok"


# @app.get("/user")
# async def list_users():

#     users = User.all()


#     return users.serialize()



# @app.get("/user/{user_id}")
# async def find_user(user_id):

#     user = User.find(user_id)

#     return user.serialize()

# @app.put("/user/{user_id}")
# async def find_user(user_id, dados: NovoUserInput):

#     user = User.find(user_id)

#     user.name = dados.name 
#     user.email = dados.email 

#     user.save()

#     return user.serialize()


# @app.delete("/user/{user_id}")
# async def delete_user(user_id):

#     user = User.find(user_id)
#     user.delete()

#     return "Deletado"

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     print("item_id: ", item_id)
#     return {"item_id": item_id, "q": q}
