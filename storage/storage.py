import logging
import yaml
from pathlib import Path

def get_configuration(configuration_type, configuration_file_path=""):
    if configuration_type == "file":
        return get_configuration_from_file(configuration_file_path)
        return 1
    logging.critical("environment variable CONFIGURATION_TYPE not provided")
    raise ValueError("configuration type should be easier file, or environment. Got {0}".format(configuration_type))

def get_configuration_from_file(configuration_file_path):
    # check that file value is set
    if configuration_file_path == "":
        logging.critical("environment variable FILE_PATH not provided, it should be when CONFIGURATION_TYPE is file")
        raise ValueError("environment variable FILE_PATH not provided, it should be when CONFIGURATION_TYPE is file")

    # Check if file exists
    configuration_file = Path(configuration_file_path)
    if not configuration_file.is_file():
        logging.critical("environment variable FILE_PATH is wrong, expected a local file, got {0}".format(configuration_file_path))
        raise ValueError("environment variable FILE_PATH not provided, it should be when CONFIGURATION_TYPE is file")


    with open(configuration_file_path, 'r') as stream:
        try:
            yaml_content = yaml.load(stream)
        except yaml.YAMLError as exc:
            logging.critical("Unable to parse file {0} as yaml".format(configuration_file_path))
            raise ValueError("Unable to parse file {0} as yaml".format(configuration_file_path))
