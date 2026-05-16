import logging

import logging


def get_logger(name: str):
    """
    Get a logger instance with the specified name.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("../logs/app.log"), logging.StreamHandler()],
    )
    return logging.getLogger(name)
