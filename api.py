from fastapi import FastAPI
#from src.search import search_tweet
app = FastAPI()

@app.get("/prueba")
def read_root():
    print("read")
    return "search_tweet(prueba' , 2)"
