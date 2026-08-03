"""
IMIS Configuration
Institutional Market Intelligence System
"""

from pathlib import Path

# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent

DATA_DIR = ROOT_DIR / "data"
LOG_DIR = ROOT_DIR / "logs"
DATABASE_DIR = ROOT_DIR / "database"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)

# --------------------------------------------------
# TRADING CONFIG
# --------------------------------------------------

SYMBOLS = [
    "XAUUSD",
    "GBPUSD",
    "USDJPY",
    "USOIL"
]

TIMEFRAMES = {
    "D1": "D1",
    "H4": "H4",
    "M15": "M15",
    "M5": "M5",
    "M1": "M1"
}

RISK_PER_TRADE = 0.01

MAX_TRADES_PER_PAIR = 2

START_SCAN_HOUR_GMT = 7

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

DATABASE_FILE = DATABASE_DIR / "imis.db"

# --------------------------------------------------

PROJECT_NAME = "IMIS"

VERSION = "1.0.0"
