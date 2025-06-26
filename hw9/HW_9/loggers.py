import logging.config
from settings import logger_set

logging.config.dictConfig(logger_set)

logger_api = logging.getLogger("api_logger")
logger_file = logging.getLogger("my_logger")
logger_console = logging.getLogger("console_logger")
