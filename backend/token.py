from dataclasses import dataclass
from typing import Tuple
import requests
import functools
import polars as pl

@dataclass
class Token:
    "Class to map tokens to company information"
    token: str
    ticker: str
    name: str
    score: float

corpus = 

def search_to_ticker(search: str) -> Token:
    tokens = search.split(" ")
    token_searches = [tokens[i:i+j] for i in range(0, len(tokens)) 
                                    for j in range(1, len(tokens) - i + 1)]
    results = list(map(lambda x: token_to_ticker(" ".join(x)), token_searches))
    return functools.reduce(lambda x, acc: x if x.score > acc.score else acc, 
                                        results, Token(search, "N/A", "N/A", 0))
    

def token_to_ticker(token: str) -> Token:
    conv_token = token.replace(" ", "%20")
    res = requests.get(f"https://ticker-2e1ica8b9.now.sh/keyword/{conv_token}").json()
    if len(res) == 0:
        return "N/A", "N/A", -1
    score = len(token.split(" ")) / len(res)
    name = res[0]['name']
    ticker = res[0]['symbol']
    return Token(token, ticker, name, score)