import unittest
from classes import configuration
import os

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

    def test_configuration__correct_environment_no_path__raise_value_error(self):
        os.environ["TERRADOC_NAME"] = "toto"
        with self.assertRaises(ValueError):
            configuration.Configuration("environment")

    def test_configuration__correct_environment_no_path__raise_value_error(self):
        os.environ["TERRADOC_NAME"] = "toto"
        os.environ["TERRADOC_PATH"] = "/data/myfiles"
        conf = configuration.Configuration("environment")
        self.assertEquals(1, len(conf.locations))
        self.assertEquals("toto", conf.locations[0].name)
        self.assertEquals("/data/myfiles", conf.locations[0].path)
        self.assertEquals(True, conf.locations[0].recursive)

    def test_set_configuration_from_file__wrong_file__raise_value_error(self):
        with self.assertRaises(ValueError):
            configuration.Configuration("")
        with self.assertRaises(ValueError):
            configuration.Configuration("somewrongfile.yml")
        with self.assertRaises(ValueError):
            configuration.Configuration("data/not_yaml.yml")
