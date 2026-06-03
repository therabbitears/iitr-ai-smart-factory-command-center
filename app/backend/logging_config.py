import logging


def setup_logging(level: int = logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    # create named logger for app
    logger = logging.getLogger('api')
    logger.setLevel(level)
    return logger
