#!/usr/bin/python3
"""tests for base_model"""
from models.base_model import BaseModel
from models import storage
import unittest
from datetime import datetime
import os

class test_basemodel(unittest.TestCase):
    def setUp(self):
        """ set/reset test environment for each test """
        storage._FileStorage__file_path = 'test_db.json'
        storage._FileStorage__objects = {}

    def tearDown(self):
        """ clear test environment after every test """
        # if os.path.exists(storage._FileStorage__file_path):
        #     os.remove(storage._FileStorage__file_path)

    def test_init(self):
        """ testing the model constructor"""
        original = BaseModel() 
        original_dict = original.to_dict()
        copy = BaseModel(**original_dict)
        copy_dict = copy.to_dict()
        self.assertEqual(original_dict, copy_dict)

        # test that a new instance is stored/tracked by storage engine
        self.assertIs(storage.all()[f'BaseModel.{original.id}'], original)

    def test_str(self):
        """ testing __str__ """
        i = BaseModel() 
        string_rep = f'[BaseModel] ({i.id}) {i.__dict__}'
        self.assertEqual(str(i), string_rep)

    def test_to_dict(self):  # TODO!!!
        """ testing to_dict"""
        i = BaseModel()
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
        i = BaseModel()
        i.save()
        self.assertNotEqual(i.created_at, i.updated_at)
