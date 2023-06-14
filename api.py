from fastapi import FastAPI
from src.search import search_tweet
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware (
    CORSMiddleware, 
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class Search(BaseModel):
    query : str
    cantidad: int




@app.get("/search")
def read_root(buscar : Search):
    response = JSONResponse(content = search_tweet(buscar.query , buscar.cantidad) , media_type="application/json")
    return response

@app.get("/prueba")
def read_root():
    response = JSONResponse(content = search_tweet("prueba " , 3) , media_type="application/json")
    return response

@app.get("/add-json")
def add_json():
    return "hola"
