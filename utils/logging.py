# src/utils/logging.py

import logging
import logging.config
import yaml

class CustomLogger:
    def __init__(self, config_file='config/logging_config.yaml'):
        self.setup_logging(config_file)

    def setup_logging(self, config_file):
        with open(config_file, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        self.logger = logging.getLogger(__name__)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

