import unittest
from storage import storage

class TestStorage(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_configuration__invalid_value__raise_value_error(self):
        with self.assertRaises(ValueError):
            storage.get_configuration("invalid_value")
        with self.assertRaises(ValueError):
            storage.get_configuration("some other value")


    def test_get_configuration__correct_type_value_no_file__raise_value_error(self):
        with self.assertRaises(ValueError):
            storage.get_configuration("file")


    def test_get_configuration_from_file__wrong_file__raise_value_error(self):
        with self.assertRaises(ValueError):
            storage.get_configuration_from_file("")
        with self.assertRaises(ValueError):
            storage.get_configuration_from_file("somewrongfile.yml")
        with self.assertRaises(ValueError):
            storage.get_configuration_from_file("data/not_yaml.yml")
