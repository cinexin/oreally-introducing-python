import logging


logging.basicConfig(level=logging.DEBUG, filename="blue_ox.log")
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warning("I need my axe")
