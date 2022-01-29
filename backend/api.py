from typing import Optional
from fastapi import FastAPI

from backend.token import search_to_ticker

app = FastAPI()

@app.get("/esg/{search}")
def aggregate_scores(search: str):
    lookup = search_to_ticker(search)
    return (lookup.ticker, lookup.name, lookup.score) # temporary just to test the deployment