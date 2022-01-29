import sqlite3
from pathlib import Path
from backend.token import Token

from ..esg_score import ESGScore

database_path = str(Path(__file__).parent / "data.db")


def initialize():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE esg (
            ticker text NOT NULL PRIMARY KEY, 
            environment real, 
            social real, 
            governance real, 
            controversy integer
        )"""
    )
    conn.commit()
    conn.close()


def get_esg(ticker: str) -> ESGScore:
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM esg WHERE ticker = ?", [ticker]).fetchone()
    if row is None:
        conn.close()
        return None
    conn.close()
    return ESGScore(row[1], row[2], row[3], row[4])


def add_esg(ticker: str, esg: ESGScore):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO esg VALUES (?, ?, ?, ?, ?)",
        [ticker, esg.environment, esg.social, esg.governance, esg.controversy],
    )
    conn.commit()
    conn.close()
