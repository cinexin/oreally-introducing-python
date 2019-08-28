import logging

format = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")
