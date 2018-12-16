import unittest
from lib import configuration


class TestStorage(unittest.TestCase):

    def setUp(self):
        pass

    def test_configuration__invalid_value__raise_value_error(self):
        with self.assertRaises(ValueError):
            configuration.Configuration("invalid_value")
        with self.assertRaises(ValueError):
            configuration.Configuration("some other value")

    def test_configuration__correct_type_value_no_file__raise_value_error(self):
        with self.assertRaises(ValueError):
            configuration.Configuration("file")


    def test_get_configuration_from_file__wrong_file__raise_value_error(self):
        with self.assertRaises(ValueError):
            configuration.Configuration("")
        with self.assertRaises(ValueError):
            configuration.Configuration("somewrongfile.yml")
        with self.assertRaises(ValueError):
            configuration.Configuration("data/not_yaml.yml")
