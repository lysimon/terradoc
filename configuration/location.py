class Location:
    def __init__(self, name=None, path=None, recursive=True):
        self.name = name
        self.path = path
        self.recursive = recursive

    def get_output(self):
        """

        :return: The markdown of all the tf file parsed by it, either one of them, or all of them if recursive was true
        """
        return 1