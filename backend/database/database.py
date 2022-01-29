from ..esg_score import ESGScore

database = {}


def get_esg(ticker: str) -> ESGScore:
    if ticker not in database:
        return None
    return database[ticker]


def add_esg(ticker: str, esg: ESGScore):
    database[ticker] = esg
