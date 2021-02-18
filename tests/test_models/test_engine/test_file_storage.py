#!/usr/bin/python3
"""Tests File"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
import pep8
from os import path
import json


class TestFileStorage(unittest.TestCase):
    """Test of Amenity_class"""

    def test_all(self):
        """Test instance of FileStorage class"""
        new_file = FileStorage()
        new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.883036",
                             updated_at="2021-02-17T22:46:38.883036")
        self.assertIsInstance(new_file, FileStorage)
        self.assertIs(type(new_file), FileStorage)
        objs = new_file.all()
        self.assertIs(type(objs), dict)

    def test_new(self):
        '''Test new method'''
        new_file = FileStorage()
        new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.883036",
                             updated_at="2021-02-17T22:46:38.883036")
        new_city = City()
        new_file.new(new_base)
        new_file.new(new_city)
        objs = new_file.all()
        key = new_base.__class__.__name__ + "." + new_base.__dict__["id"]
        key_2 = new_city.__class__.__name__ + "." + new_city.__dict__["id"]
        self.assertIn(key, objs)
        self.assertIn(key_2, objs)

    def test_save(self):
        '''Test save method'''
        new_file = FileStorage()
        new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.883036",
                             updated_at="2021-02-17T22:46:38.883036")
        new_city = City()
        new_file.new(new_base)
        new_file.new(new_city)
        new_file.save()
        self.assertTrue(path.exists("file.json"))
        self.assertTrue(path.isfile("file.json"))
        self.assertFalse(path.isdir("file.json"))
        with open("file.json", "r") as f:
            self.assertTrue(type(json.load(f)), str)

    def test_reload(self):
        '''Test upload method'''
        if not path.exists("file.json"):
            new_file = FileStorage()
            new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.86",
                                 updated_at="2021-02-17T22:46:38.86")
            new_city = City()
            new_file.new(new_base)
            new_file.new(new_city)
            new_file.save()
        with open("file.json", "r") as f:
            obj = json.load(f)
        self.assertEqual(type(obj), dict)


if __name__ == "__main__":
    unittest.main()
