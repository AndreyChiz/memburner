import logging
import sys
from pathlib import Path
from loguru import logger
import json
import os
from context_vars import request_id_var

# template:
# https://medium.com/1mgofficial/how-to-override-uvicorn-logger-in-fastapi-using-loguru-124133cdcd4e


class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: "CRITICAL",
        40: "ERROR",
        30: "WARNING",
        20: "INFO",
        10: "DEBUG",
        0: "NOTSET",
    }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        log = logger.bind(request_id=request_id_var.get())
        log.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


class CustomLogger:

    @classmethod
    def make_logger(
        cls,
        path: str,
        file_name_perfix: str,
        level: str,
        rotation: str,
        retention: str,
        log_format: str,
        compression: str,
    ):

        os.makedirs(path, exist_ok=True)

        logger.remove()
        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=log_format,
        )
        logger.add(
            os.path.join(
                path,
                f"{file_name_perfix}_" + f"level_{level}_" + "{time:YYYY-MM-DD}.log",
            ),
            rotation=rotation,
            retention=retention,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=log_format,
            compression=compression,
        )
        logging.basicConfig(handlers=[InterceptHandler()], level=0)
        logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
        for _log in ["uvicorn", "uvicorn.error", "fastapi"]:
            _logger = logging.getLogger(_log)
            _logger.handlers = [InterceptHandler()]

        return logger.bind(request_id=None, method=None)
