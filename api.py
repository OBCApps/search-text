from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import json
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List , Dict, Any
from src.search import search_tweet, search_tweet_web
from src.inverted_index import create_index_of_web, create_invert_index
import traceback


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




@app.post("/search-local")
async def search_local(buscar : Search):
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


@app.post("/search-web")
async def search_web(buscar: Search):
    json_data = {}
    try:
        print("buscar", buscar)
        inicio = time.time()
        response = search_tweet_web(buscar.query, buscar.cantidad)
        fin = time.time()

        json_data = {
            "tiempo_ejecucion": fin - inicio,
            "respuesta": response,
        }

        return json_data
    except Exception as e:
        error_message = traceback.format_exc()
        json_data["respuesta"] = f"Error al cargar los datos: {error_message}"
        return json_data


""" @app.get("/prueba")
def dev():
    #response = JSONResponse(content = search_tweet("prueba " , 3) , media_type="application/json")
    response = search_tweet("prueba " , 3)
    return response """


@app.get("/add-js-local")
async def add_local():
  
    json_data = {}
    inicio = time.time()

    try:
        create_invert_index()
        json_data["respuesta"] = "Datos cargados correctamente"
    except Exception as e:
        json_data["respuesta"] = f"Error al cargar los datos: {str(e)}"
    
    fin = time.time()

    json_data["tiempo_ejecucion"] = fin - inicio

    return json_data




@app.post("/add-json-web")
async def add_web(data: List[List[Dict[str, Any]]]):
    #print("data" , data)
    json_data = {}
    inicio = time.time()

    try:
        create_index_of_web(data)
        json_data["respuesta"] = "Datos cargados correctamente"
    except Exception as e:
        json_data["respuesta"] = f"Error al cargar los datos: {str(e)}"
    
    fin = time.time()

    json_data["tiempo_ejecucion"] = fin - inicio

    return json_data