import logging
import json

def get_configuration(configuration_type, configuration_file_path=""):
    if configuration_type == "file":
        if configuration_file_path == "":
            logging.critical("environment variable FILE_PATH not provided, it should be when CONFIGURATION_TYPE is file")
            raise ValueError(
                "configuration type should be easier file, or environment. Got {0}".format(configuration_type))
        return get_configuration_from_file(configuration_file_path)
        return 1

    logging.critical("environment variable CONFIGURATION_TYPE not provided")
    raise ValueError("configuration type should be easier file, or environment. Got {0}".format(configuration_type))

def get_configuration_from_file(configuration_file_path):
    with open('filename.txt', 'r') as f:
        array = json.load(f)
    print(array)