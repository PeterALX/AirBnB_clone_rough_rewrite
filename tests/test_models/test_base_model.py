#!/usr/bin/python3
"""tests for base_model"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """ makes a BaseModel instance before each test """
        self.test_model = BaseModel()

    def tearDown(self):
        """ destroys the BaseModel instance after each test """
        del self.test_model

    def test_str(self):
        """ testing __str__ """
        i = self.test_model
        string_rep = f'[BaseModel] ({i.id}) {i.__dict__}'
        self.assertEqual(str(i), string_rep)

    def test_to_dict(self):  # TODO!!!
        """ testing to_dict"""
        i = self.test_model
