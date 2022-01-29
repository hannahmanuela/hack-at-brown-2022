import dataclasses

import requests

from .esg import get_esg


def search_to_ticker(search: str):
    tokens = search.split(" ")
    token_searches = [
        " ".join(tokens[i : i + j])
        for i in range(0, len(tokens))
        for j in range(1, len(tokens) - i + 1)
    ]
    tickers = [
        entry for entry in map(token_to_ticker, token_searches) if entry is not None
    ]

    if len(tickers) == 0:
        return None

    best_ticker = max(tickers, key=lambda ticker: ticker["score"])
    esg = get_esg(best_ticker["ticker"])
    if esg is None:
        return None
    return {
        "name": best_ticker["name"],
        "ticker": best_ticker["ticker"],
        "esg": dataclasses.asdict(esg),
    }


def token_to_ticker(token: str):
    query = f"https://ticker-2e1ica8b9.now.sh/keyword/{requests.utils.quote(token)}"
    r = requests.get(query)
    if not r.ok:
        raise RuntimeError("Failed to query " + query)
    res = r.json()
    if len(res) == 0:
        return None
    return_entry = res[0]
    return {
        "name": return_entry["name"],
        "ticker": return_entry["symbol"],
        "score": len(token.split(" ")) / len(res),
    }
