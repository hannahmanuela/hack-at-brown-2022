import backend.database as database
import yfinance as yf

from ..esg_score import ESGScore


def get_esg_api(ticker: str) -> ESGScore:
    ticker = yf.Ticker(ticker)
    df = ticker.get_sustainability()
    if df is None:
        return None
    return ESGScore(
        df["Value"]["environmentScore"],
        df["Value"]["socialScore"],
        df["Value"]["governanceScore"],
        df["Value"]["highestControversy"],
    )


def get_esg(ticker: str) -> ESGScore:
    # check database caching first
    esg = database.get_esg(ticker)
    if esg:
        return esg
    # hit api if database does not have entry
    esg = get_esg_api(ticker)

    if not esg:
        return None
    # cache results before returning
    database.add_esg(ticker, esg)
    return esg
