import logging
import yaml
import os
from classes import location
from pathlib import Path

class Configuration(object):

    def __init__(self, configuration_type, configuration_file_path=""):
        self.locations = []
        if configuration_type == "file":
            self.set_configuration_from_file(configuration_file_path)
        elif configuration_type == "environment":
            self.set_configuration_from_environment()
        else:
            logging.critical("environment variable CONFIGURATION_TYPE not provided")
            raise ValueError("classes type should be easier file, or environment. Got {0}".format(configuration_type))

        if len(self.locations) == 0:
            raise ValueError("No location was defined")

    def set_configuration_from_environment(self):
        # Get all environment variables
        environment_variable_names = os.environ
        path_name = "TERRADOC_NAME"
        path_prefix = "TERRADOC_PATH"
        recursive_prefix = "TERRADOC_RECURSIVE"

        for environment_variable_name in environment_variable_names:

            if environment_variable_name.startswith(path_name):
                suffix = environment_variable_name[len(path_name):]
                name = os.environ.get(path_name + suffix)
                path = os.environ.get(path_prefix + suffix)
                recursive = (os.environ.get(recursive_prefix + suffix) != "false")
                location2 = location.Location(name, path, recursive)
                self.locations.append(location2)

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

        raise ValueError("file classes is not implemented yet")
