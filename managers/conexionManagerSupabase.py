import os
from typing import Generator

import psycopg
from dotenv import load_dotenv

load_dotenv()
passwordDB  =  os.getenv("PASSWORD")

def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")

    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()