import json
import csv
import logging
from logging.handlers import RotatingFileHandler

# Logging setup
def setup_logging(log_file='app.log', level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)

    # Rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

# Configuration file parsing
def parse_config(config_file):
    try:
        with open(config_file, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error parsing config file: {e}")
        raise

# Data format conversions
def json_to_dict(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding error: {e}")
        raise

def csv_to_list(csv_file):
    try:
        with open(csv_file, newline='') as file:
            return list(csv.reader(file))
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        raise

# Error handling utility
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper

