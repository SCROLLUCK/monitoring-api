import logging
import uvicorn 
import sys
from copy import copy
from logging import config
from termcolor import colored

terminal_colors = {
    logging.DEBUG: "cyan",
    logging.INFO: "light_blue",
    logging.WARNING: "yellow",
    logging.ERROR: "red",
    logging.CRITICAL: "magenta"
}

LOGGING = dict(
    version=1,
    disable_existing_loggers=True,
    loggers=dict(
        logger=dict(
            level="INFO",
            propagate=True
        )
    )
)

config.dictConfig(LOGGING)

for level, color in terminal_colors.items():

    level_str = colored(
        logging.getLevelName(level), color, attrs=["bold"]
    )
    logging.addLevelName(level, level_str.center(20))


logger = logging.getLogger("logger")
handler = logging.StreamHandler(stream=sys.stdout)

class ColoredFormatter(logging.Formatter):
    
    def __init__(self, pattern, datefmt, style):
        logging.Formatter.__init__(
            self,
            fmt=pattern,
            datefmt=datefmt,
            style=style
        )

    def format(self, record: logging.LogRecord):
        colored_record = copy(record)

        colored_record.levelname = colored(
            colored_record.levelname,
            terminal_colors.get(
                colored_record.levelno
            ),
            attrs=["bold"]
        )

        colored_record.msg = colored(
            colored_record.msg,
            terminal_colors.get(
                colored_record.levelno
            ),
            attrs=["bold"]
        )

        return logging.Formatter.format(self, colored_record)
    

formatter = ColoredFormatter(
    "%(asctime)s.%(msecs)03d "
    "%(levelname)s "
    "%(process)-8s "
    "%(name)-15s > "
    "%(message)s",
    "%d-%m-%Y %H:%M:%S",
    "%"
)

handler.setFormatter(
    formatter
)

logger.addHandler(handler)

uvicorn.config.logger.addHandler(handler)
uvicorn.config.LOGGING_CONFIG["formatters"]["access"][
    "datefmt"] = formatter.datefmt
uvicorn.config.LOGGING_CONFIG["formatters"]["access"]["fmt"] = formatter._fmt
uvicorn.config.LOGGING_CONFIG["formatters"]["default"][
    "datefmt"] = formatter.datefmt
uvicorn.config.LOGGING_CONFIG["formatters"]["default"]["fmt"] = formatter._fmt
uvicorn.config.LOGGING_CONFIG["formatters"]["default"]["use_colors"] = True
