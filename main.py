from config import (
    PROJECT_NAME,
    VERSION,
    SYMBOLS
)

from utils.logger import log
from database.db import Database
from engines.data_engine import DataEngine


def startup():

    log.info("=" * 60)

    log.info(f"{PROJECT_NAME} v{VERSION}")

    log.info("Institutional Market Intelligence System")

    log.info("=" * 60)

    db = Database()
    data = DataEngine()

    log.info("Database Loaded")
    log.info("Data Engine Loaded")

    log.info("Watching Symbols:")

    for symbol in SYMBOLS:

        log.info(f"   {symbol}")

    log.info("=" * 60)


def main():

    startup()

    log.info("IMIS Core Loaded Successfully")


if __name__ == "__main__":

    main()
    
