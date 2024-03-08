import logging

def setup_debug_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) 
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(handler)
    return logger