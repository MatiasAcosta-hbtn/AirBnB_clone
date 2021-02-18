#!/usr/bin/python3
"""Tests File"""
import unittest
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """Test of User class"""

    def test_User(self):
        """Test instance of User class"""
        new = User()
        new2 = User()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), User)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)

    def test_attr(self):
        new = User()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "email"))
        self.assertEqual(type(new.email), str)
        self.assertNotEqual(type(new.email), int)
        self.assertNotEqual(type(new.email), list)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

if __name__ == "__main__":
    unittest.main()
