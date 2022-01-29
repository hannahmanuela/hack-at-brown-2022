from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/esg/{search}")
def aggregate_scores(search: str):
    pass