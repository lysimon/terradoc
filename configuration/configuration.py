import logging
import yaml
from pathlib import Path

class Location(object):
    def __init__(self, name, path, prefix="", recursive=True):
        self.name = name
        self.path = path
        self.prefix = prefix
        self.recursive = recursive

class Configuration(object):

    def __init__(self, configuration_type, configuration_file_path=""):
        if configuration_type == "file":
            self.set_configuration_from_file(configuration_file_path)
        elif configuration_type == "environment":
            self.set_configuration_from_environment()

        logging.critical("environment variable CONFIGURATION_TYPE not provided")
        raise ValueError("configuration type should be easier file, or environment. Got {0}".format(configuration_type))

    def set_configuration_from_environment(self):
        # Get all environment variables

        return 1

    def set_configuration_from_file(self, configuration_file_path):
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

        raise ValueError("file configuration is not implemented yet")
