from dataclasses import dataclass, asdict
import re
import pandas as pd

from .esg import get_esg

corpus = pd.read_csv("tickers.csv")
names = corpus.Name.tolist()
ticks = corpus.Symbol.tolist()

@dataclass
class Token:
    "Class to map tokens to company information"
    token: str
    ticker: str
    name: str
    score: float


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

    best_ticker = max(tickers, key=lambda ticker: ticker.score)
    esg = get_esg(best_ticker.ticker)
    if esg is None:
        return None
    return {
        "name": best_ticker.name,
        "ticker": best_ticker.ticker,
        "esg": asdict(esg),
    }


def scoring(match: str, token: str) -> float:
    if match.startswith(token):
        return 3
    elif match.endswith(token):
        return 2
    elif re.fullmatch(token, match) is not None:
        return 1
    else:
        return 0

def token_to_ticker(token: str) -> Token:
    idxs = list(filter(lambda i: token.lower() in names[i].lower(), range(len(names))))
    scores = list(map(lambda x: scoring(names[x], token), idxs))
    idxs = [x for _, x in sorted(zip(scores, idxs), key=lambda pair: pair[0], reverse=True)]
    res = zip(map(lambda i: names[i], idxs), map(lambda i: ticks[i], idxs))
    if len(idxs) == 0:
        return None
    return_entry = next(res)
    return Token(
        token,
        return_entry[1],
        return_entry[0],
        len(token.split(" ")) / len(idxs)
    )
