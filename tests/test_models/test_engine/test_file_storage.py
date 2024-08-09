#!/usr/bin/python3
"""tests for the file storage engine"""
from models import storage
from models.base_model import BaseModel
import unittest
import os
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """ set/reset test environment for each test """
        storage._FileStorage__file_path = 'test_db.json'
        storage._FileStorage__objects = {}

    def tearDown(self):
        """ clear test environment after every test """
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_new(self):
        """ test new object addition on instantiation """
        i = BaseModel()
        self.assertIs(storage.all()[f'BaseModel.{i.id}'], i)

    def test_save(self):
        """ test that storage.save serializes models to json properly """
        i = BaseModel()
        d = i.to_dict()
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            json_dict = json.load(f)
            self.assertEqual(json_dict[f'BaseModel.{i.id}'], d)
