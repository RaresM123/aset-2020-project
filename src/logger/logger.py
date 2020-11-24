import logging
from logging import handlers
import os


def get_logger():
    """
    Initializes the logger
    :return:
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(script_dir, 'logs')
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    log_path = os.path.join(log_dir, 'aset_project.log')
    _logger = logging.getLogger("aset_project")
    _logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s][%(name)s][%(thread)d][%(funcName)s][%(levelname)s] %(message)s')

    file_handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=1024 ** 2, backupCount=6)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)

    return _logger


LOGGER = get_logger()
