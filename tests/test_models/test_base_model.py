#!/usr/bin/python3
"""tests for base_model"""
from models.base_model import BaseModel
from models import storage
import unittest
from datetime import datetime
import os
import json


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """ set/reset test environment for each test """
        storage._FileStorage__file_path = 'test_db.json'
        storage._FileStorage__objects = {}

    def tearDown(self):
        """ clear test environment after every test """
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

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
        model = BaseModel()
        string_rep = f'[BaseModel] ({model.id}) {model.__dict__}'
        self.assertEqual(str(model), string_rep)

    def test_to_dict(self):  # TODO!!!
        """ testing to_dict"""
        model = BaseModel()
        d = model.to_dict()
        self.assertEqual(d['__class__'], model.__class__.__name__)
        for k, v in model.__dict__.items():
            message = f'property \'{k}\' missing from \
dictionary representation of BaseModel'
            self.assertIn(k, d, msg=message)
            if type(v) is datetime:
                self.assertIsInstance(d[k], str)
                self.assertIsInstance(datetime.fromisoformat(d[k]), datetime)

    def test_save(self):
        """ testing BaseModel's save """
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)

        # test that model is saved to json properly
        d = model.to_dict()
        with open(storage._FileStorage__file_path, 'r') as f:
            json_dict = json.load(f)
            self.assertEqual(json_dict[f'BaseModel.{model.id}'], d)
