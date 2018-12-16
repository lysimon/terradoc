import logging

class Location:
    def __init__(self, name=None, path=None, recursive=True):
        if name is None or name == "":
            raise ValueError("Name should not be null")
        if path is None or path == "":
            raise ValueError("Path should not be null")

        self.name = name
        self.path = path
        self.recursive = recursive
        logging.info("Location(name={0}, path={1}, recursive={2}".format(name, path, recursive))

    def get_output(self):
        """

        :return: The markdown of all the tf file parsed by it, either one of them, or all of them if recursive was true
        """
        return 1