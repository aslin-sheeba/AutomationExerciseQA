import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

_log_file = os.path.join("logs", f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(_log_file),
        logging.StreamHandler(),
    ],
)


def get_logger(name):
    return logging.getLogger(name)
