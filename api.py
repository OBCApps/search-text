from fastapi import FastAPI
from src.search import search_tweet
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware (
    CORSMiddleware, 
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/search")
def read_root():
    
    return search_tweet('prueba de amor' , 2)
