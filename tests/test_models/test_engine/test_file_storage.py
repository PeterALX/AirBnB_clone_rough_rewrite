#!/usr/bin/python3
"""tests for the file storage engine"""
from models import storage 
from models.base_model import BaseModel
import unittest
import os

print(storage.all().keys())

class test_filestorage(unittest.TestCase):
    def setUp(self):
        """ makes a BaseModel instance before each test """
        self.test_model = BaseModel()

    def tearDown(self):
        """ destroys the BaseModel instance after each test """
        del self.test_model
        # os.remove(storage._FileStorage__file_path)

    def test_new(self):
        """ test new object addition on instantiation """
        i = self.test_model
        self.assertIs(storage.all()[f'BaseModel.{i.id}'], i)

    def test_save(self):
        pass





