#!/usr/bin/python3
"""Tests File"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """Test of Place class"""

    def test_Place(self):
        """Test instance of amenity class"""
        new = Place()
        new2 = Place()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), Place)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)

    def test_Place_init(self):
        """Test Init with Kwargs"""
        new = Place(id="123", created_at="2021-02-17T22:46:38.883036",
                        updated_at="2021-02-17T22:46:38.883036")
        new2 = Place(id="123", name="Matias tu papi")
        self.assertFalse(hasattr(new2, "created_at"))
        self.assertTrue(hasattr(new2, "name"))
        self.assertEqual(new.id, "123")

    def test_attr(self):
        new = Place()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "city_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "description"))
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertTrue(hasattr(new, "latitude"))
        self.assertTrue(hasattr(new, "longitude"))
        self.assertTrue(hasattr(new, "amenity_ids"))
        self.assertEqual(type(new.amenity_ids), list)
        self.assertNotEqual(type(new.city_id), int)
        self.assertEqual(type(new.name), str)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_method_str(self):
        """Test method str"""
        new = Place()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertTrue(type(new.__str__()), str)
        self.assertTrue(len(new.__str__()))

    def test_to_dict(self):
        new = Place()
        dict_new = new.to_dict()
        self.assertNotEqual(new.__dict__, new.to_dict())
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertTrue("__class__" in dict_new)
        self.assertEqual(dict_new["__class__"],  "Place")

    def test_save(self):
        new = Place()
        created = new.updated_at
        new.save()
        updated = new.updated_at
        self.assertNotEqual(updated, created)
        self.assertGreater(updated, created)

if __name__ == "__main__":
    unittest.main()
