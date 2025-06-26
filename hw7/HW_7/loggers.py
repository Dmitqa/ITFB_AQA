import logging.config
from hw7.settings import logger_set

logging.config.dictConfig(logger_set)

logger_file = logging.getLogger("my_logger")
logger_console = logging.getLogger("console_logger")
