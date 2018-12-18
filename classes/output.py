import logging
import json
class Output:
    def __init__(self, tfstate_data):
        """

        :param tfstate_data:
        """
        json_data = json.loads(tfstate_data)
        print(json_data['version'])
        self.content = "toto"

    def get_by_category(self):
        """

        :return: The markdown of all the tf file parsed by it, either one of them, or all of them if recursive was true
        """
        return 1