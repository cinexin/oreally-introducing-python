import logging

# DEBUG and INFO logs won't be shown since default log level is WARNING
logging.debug("Looks like rain")
logging.info("And hail")
logging.warning("Did I hear thunder?")
logging.error("Was that lightning?")
logging.critical("Stop fencing and get inside!")

# how can we enable DEBUG level?

logging.getLogger().setLevel(logging.DEBUG)
logging.debug("It's raining again")
logging.info("With hail the size of hailstonews")