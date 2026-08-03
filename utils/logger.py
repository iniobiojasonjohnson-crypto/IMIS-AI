from pathlib import Path
from loguru import logger

LOG_FOLDER = Path("logs")
LOG_FOLDER.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_FOLDER / "imis.log",
    rotation="5 MB",
    retention="30 days",
    level="INFO",
    enqueue=True
)

logger.add(
    lambda msg: print(msg, end=""),
    level="INFO"
)

log = logger
