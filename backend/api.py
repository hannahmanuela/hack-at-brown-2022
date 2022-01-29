from fastapi import FastAPI, Response, status

from backend.token import search_to_ticker

app = FastAPI()


@app.get("/esg/{search}")
def aggregate_scores(search: str, response: Response):
    score = search_to_ticker(search)
    if score is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    return score
