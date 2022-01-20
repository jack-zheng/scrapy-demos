import logging

logging.basicConfig(
    filemode="w",
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("This is a log...")
    logger.info("This is a log2...")