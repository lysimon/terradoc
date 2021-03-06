import os
import logging
from classes import configuration

LOG_LEVEL = os.getenv("LOG_LEVEL")
if LOG_LEVEL == "DEBUG":
    logging.getLogger().setLevel(logging.DEBUG)
elif LOG_LEVEL == "INFO":
    logging.getLogger().setLevel(logging.INFO)
elif LOG_LEVEL == "WARNING":
    logging.getLogger().setLevel(logging.WARNING)
elif LOG_LEVEL == "CRITICAL":
    logging.getLogger().setLevel(logging.CRITICAL)
elif LOG_LEVEL is None:
    print("Default log level set to INFO as no LOG_LEVEL value has been provided")
    logging.getLogger().setLevel(logging.INFO)
else:
    raise ValueError("Expecting LOG_LEVEL with value inside DEBUG, INFO, WARNING or CRITICAL, got {0}".format(LOG_LEVEL))


logging.info("Starting Terradoc")

# Step 1, read all the classes
logging.info("Step 1: Initializing configuration")
conf = configuration.Configuration(os.environ.get("CONFIGURATION_TYPE"), os.environ.get("FILE_PATH"))
logging.info("Step 2: Fetching output files")
outputs = conf.get_outputs()
# Generate all the output