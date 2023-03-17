from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message":"Servidor ejecutandose"}

usuarios = [
    {'id':1,
    'username':'reinel',
     'password':'quiz'
     },
     {'id':2,
    'username':'james',
     'password':'jajaja'
     },
     {'id':3,
    'username':'johan',
     'password':'pina'
     },
     {'id':4,
    'username':'camilo',
     'password':'1234'
     },
     {'id':5,
    'username':'chatgpt',
     'password':'version4'
     }
]

@app.get("/user/all/")
def listar_allUsers():
    return usuarios

@app.get("/user/unique/{id_usuario}")
def listar_justOne(id_usuario:int):
    # buscar el usuario en la lista

    for user in usuarios:
        if user['id'] == id_usuario:
            return user
    return {"message":"No se encontró el usuario en la DB"}


