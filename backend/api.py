from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from backend.search import search_to_ticker

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/esg/{search}")
def aggregate_scores(search: str, response: Response):
    score = search_to_ticker(search)
    if score is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    return score
