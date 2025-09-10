from loguru import logger
from .settings import settings

def setup_logging() -> None:
    logger.remove()
    logger.add(lambda m: print(m, end=""), level=settings.LOG_LEVEL)

setup_logging()  # side-effect: configure on import
