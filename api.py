from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import json
from src.search import search_tweet
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List

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




@app.post("/search")
async def read_root(buscar : Search):
    try:
        print("buscar" , buscar)
        #response = JSONResponse(content = search_tweet(buscar.query , buscar.cantidad) , media_type="application/json")
        inicio = time.time()
        response = search_tweet(buscar.query , buscar.cantidad)
        fin = time.time()

        json_data = {            
            "tiempo_ejecucion": fin - inicio,
            "respuesta":  response,
        }
                
        return json_data
    except KeyError:
        raise HTTPException(status_code=404, detail="La palabra no fue encontrada")


@app.get("/prueba")
def read_root():
    #response = JSONResponse(content = search_tweet("prueba " , 3) , media_type="application/json")
    response = search_tweet("prueba " , 3)
    return response




@app.post("/add-json")
async def add_json(data: List[dict]):    
    print(data)
    for item in data:
        value1 = item["id"]
        value2 = item["text"]
        print(f"id: {value1} | id: {value2}")
        
        
        
    return {"message": "Datos recibidos correctamente"}
