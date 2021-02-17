#!/usr/bin/ python3
"""Tests File"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import pep8


class TestBaseModel(unittest.TestCase):
    """Test of Base Model class"""

    def test_BaseModel(self):
        """Test instance of BaseClass class"""
        new = BaseModel()
        new2 = BaseModel()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), BaseModel)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)

    def test_attr(self):
        """Test Attributes of the instance"""
        new = BaseModel()
        new.name = "Matias Tu Papi"
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_id(self):
        """test if uuid is a string"""
        new = BaseModel()
        self.assertIsInstance(new.id, str)

    def test_created_at(self):
        """test created_at format"""
        new = BaseModel()
        self.assertIsInstance(new.created_at, datetime)

    def test_updated_at(self):
        """test updated_at format"""
        new = BaseModel()
        self.assertIsInstance(new.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
