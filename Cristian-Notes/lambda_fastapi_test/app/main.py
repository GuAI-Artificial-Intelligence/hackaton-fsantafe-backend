from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/guai-test")
def hello_world():
    return {"hello": "world"}

@app.get("/paula")
def hello_world():
    return {"hello": "Paula"}

@app.get("/cristian")
def hello_world():
    return {"hello": "Cristian"}

handler = Mangum(app)
