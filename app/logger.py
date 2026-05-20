# import logging


# def get_logger(name: str):
#     """
#     Get a logger instance with the specified name.
#     """

#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#         handlers=[logging.FileHandler("../logs/app.log"), logging.StreamHandler()],
#     )
#     return logging.getLogger(name)


import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
