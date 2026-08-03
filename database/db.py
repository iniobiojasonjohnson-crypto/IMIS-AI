import sqlite3
from pathlib import Path

DB_PATH = Path("database/imis.db")

class Database:

    def __init__(self):

        DB_PATH.parent.mkdir(exist_ok=True)

        self.conn = sqlite3.connect(DB_PATH)

        self.create_tables()

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS trades(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            direction TEXT,

            entry REAL,

            sl REAL,

            tp REAL,

            result TEXT,

            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        self.conn.commit()

    def close(self):

        self.conn.close()
