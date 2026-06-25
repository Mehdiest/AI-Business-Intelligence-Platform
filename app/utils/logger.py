from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", enqueue=True, backtrace=False, diagnose=False)
