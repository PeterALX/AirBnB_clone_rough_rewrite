#!/usr/bin/python3
"""tests for the file storage engine"""
from models import storage 
from models.base_model import BaseModel
import unittest

print(storage.all().keys())

class test_filestorage(unittest.TestCase):
    def setUp(self):
        """ makes a BaseModel instance before each test """
        self.test_model = BaseModel()

    def tearDown(self):
        """ destroys the BaseModel instance after each test """
        del self.test_model

    def test_new(self):
        model = BaseModel()


