import logging
from pathlib import Path
import logging.config


# Defines
CONFIG_FILE = 'logging_config.ini'

logging_config = Path(__file__).parent / CONFIG_FILE
logging.config.fileConfig(logging_config)


class Logger(object):

    def __new__(cls, module_name: str, *args, **kwargs):
        logger = logging.getLogger(module_name)

        return logger
