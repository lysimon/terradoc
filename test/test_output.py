import unittest
from classes import configuration, location, output
import os

class TestStorage(unittest.TestCase):

    def setUp(self):
        pass

    def test_output__valid_tfstatefile_returnsoutput(self):
        with open('data/tfstate/test1/terraform.tfstate', 'r') as myfile:
            data = myfile.read()
        out = output.Output(data)
        self.assertEqual("this is just a tribute", out.content)