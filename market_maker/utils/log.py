import logging
from logging.handlers import TimedRotatingFileHandler
from market_maker.settings import settings
import os
from pathlib import Path


def setup_custom_logger(name, log_file=settings.LOG_FILE,
                        log_level=settings.LOG_LEVEL):
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )
    logger = logging.getLogger(name)
    # different log levels for file and console handlers require
    # to set root logger to lowest level, ie logging.DEBUG
    logger.setLevel(logging.DEBUG)

    # log to stdout, ie console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)
    logger.addHandler(console_handler)

    # if LOG_FILE provided, then log errors to file
    if log_file:
        # root dir of project
        root = Path(__file__).parent.parent.parent.resolve()
        log_file = os.path.join(root, log_file)
        
        # check if we need to create a sub dir for logs
        log_dir, _ = os.path.split(log_file)
        if log_dir:
            os.makedirs(os.path.join(root, log_dir), exist_ok=True)
        
        file_handler = TimedRotatingFileHandler(log_file, when='d',
                                                interval=1, backupCount=7)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.ERROR)
        logger.addHandler(file_handler)
    
    return logger
