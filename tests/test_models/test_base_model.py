#!/usr/bin/python3
"""tests for base_model"""
from models.base_model import BaseModel
from models import storage
import unittest
from datetime import datetime

# print(storage._FileStorage__file_path)
# print(storage._FileStorage__objects)
class test_basemodel(unittest.TestCase):
    def setUp(self):
        """ makes a BaseModel instance before each test """
        self.test_model = BaseModel()

    def tearDown(self):
        """ destroys the BaseModel instance after each test """
        del self.test_model

    def test_init(self):
        """ testing the model constructor"""
        original = self.test_model
        original_dict = original.to_dict()
        copy = BaseModel(**original_dict)
        copy_dict = copy.to_dict()
        self.assertEqual(original_dict, copy_dict)

    def test_str(self):
        """ testing __str__ """
        i = self.test_model
        string_rep = f'[BaseModel] ({i.id}) {i.__dict__}'
        self.assertEqual(str(i), string_rep)

    def test_to_dict(self):  # TODO!!!
        """ testing to_dict"""
        i = self.test_model
        d = i.to_dict()
        self.assertEqual(d['__class__'], i.__class__.__name__)
        for k, v in i.__dict__.items():
            message = f'property \'{k}\' missing from \
dictionary representation of BaseModel'
            self.assertIn(k, d, msg=message)
            if type(v) is datetime:
                self.assertIsInstance(d[k], str)
                self.assertIsInstance(datetime.fromisoformat(d[k]), datetime)

    def test_save(self):
        """ testing save """
        i = self.test_model
        i.save()
        self.assertNotEqual(i.created_at, i.updated_at)
