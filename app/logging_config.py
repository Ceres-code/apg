import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logging.basicConfig(filename='application.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler('application.log', maxBytes=1000000, backupCount=5)
    logger.addHandler(handler)
    return logger



