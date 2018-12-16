def get_configuration(configuration_type, configuration_file_path=""):
    if configuration_type == "file":
        return 1

    raise ValueError("configuration type should be easier file, or environment. Got {0}".format(configuration_type))
