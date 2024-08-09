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
        model = BaseModel()
        self.assertIs(storage.all()[f'BaseModel.{model.id}'], model)

    def test_save(self):
        """ test that storage.save serializes models to json properly """
        model = BaseModel()
        d = model.to_dict()
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            json_dict = json.load(f)
            self.assertEqual(json_dict[f'BaseModel.{model.id}'], d)

    def test_reload(self):
        """ test that storage.save serializes models to json properly """
        model = BaseModel()
        d = model.to_dict()
        storage.save()
        len_before_reload = len(storage.all())
        storage.reload()
        len_after_reload = len(storage.all())

        reloaded_model = storage.all()[f'BaseModel.{model.id}']
        self.assertIsNot(reloaded_model, model)
        self.assertEqual(reloaded_model.to_dict(), d)

        self.assertEqual(len_before_reload, len_after_reload)

    def test_filepath(self):
        """
        Test that storage engine's file path is present and a string
        """
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_objects(self):
        """
        Test that storage engine's __objects is present and a dict
        """
        self.assertIsInstance(storage._FileStorage__objects, dict)
