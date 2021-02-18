#!/usr/bin/python3
"""Tests File"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
import pep8


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
    
    def test_reload(self):
        '''Test upload method'''



if __name__ == "__main__":
    unittest.main()
