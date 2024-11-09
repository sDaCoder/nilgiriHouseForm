# Code for Backend
# Packages installed -> FastAPI and uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/item")
async def get_items(I: Item):
    dic = {"message": "Success", **I.dict()}
    print(dic)
    return dic

@app.get("/{name}")
def hello(name: str):
    return {"message": f"Hello {name}"}
