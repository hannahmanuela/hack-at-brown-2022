from typing import Optional
from fastapi import FastAPI

from backend.company import search_to_ticker

app = FastAPI()

@app.get("/esg/{search}")
def aggregate_scores(search: str):
    ticker, name, score = search_to_ticker(search)
    return (ticker, name, score) # temporary just to test the deployment