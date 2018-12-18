import unittest
from classes import configuration, location
import os

class TestStorage(unittest.TestCase):

    def setUp(self):
        pass

    def test_location__invalid_value__raise_value_error(self):
        with self.assertRaises(ValueError):
            location.Location()
        with self.assertRaises(ValueError):
            location.Location("")
        with self.assertRaises(ValueError):
            location.Location("aa")
        with self.assertRaises(ValueError):
            location.Location("aa", "")

    def test_location__correct_value_successful(self):
        loc = location.Location("someName", "somePath")
        self.assertEqual("someName", loc.name)
        self.assertEqual("somePath", loc.path)
        self.assertTrue(loc.recursive)

        loc = location.Location("someName", "somePath", False)
        self.assertEqual("someName", loc.name)
        self.assertEqual("somePath", loc.path)
        self.assertFalse(loc.recursive)