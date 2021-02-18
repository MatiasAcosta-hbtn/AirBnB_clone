#!/usr/bin/python3
"""Tests File"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
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
        new_amenity = Amenity()
        new_user = User()
        new_place = Place()
        new_review = Review()
        new_state = State()
        new_file.new(new_base)
        new_file.new(new_city)
        new_file.new(new_amenity)
        new_file.new(new_place)
        new_file.new(new_state)
        new_file.new(new_user)
        new_file.new(new_review)
        objs = new_file.all()
        key = new_base.__class__.__name__ + "." + new_base.__dict__["id"]
        key_2 = new_city.__class__.__name__ + "." + new_city.__dict__["id"]
        key_user = new_user.__class__.__name__ + "." + new_user.__dict__["id"]
        key_review = new_review.__class__.__name__ + "." + new_review.__dict__["id"]
        key_place = new_place.__class__.__name__ + "." + new_place.__dict__["id"]
        key_state = new_state.__class__.__name__ + "." + new_state.__dict__["id"]
        key_amenity = new_amenity.__class__.__name__ + "." + new_amenity.__dict__["id"]
        self.assertIn(key, objs)
        self.assertIn(key_2, objs)
        self.assertIn(key_user, objs)
        self.assertIn(key_review, objs)
        self.assertIn(key_place, objs)
        self.assertIn(key_state, objs)
        self.assertIn(key_amenity, objs)

    def test_save(self):
        '''Test save method'''
        objs = models.storage
        new_base = BaseModel()
        new_user = User()
        new_state = State()
        new_place = Place()
        new_city = City()
        new_amenity = Amenity()
        new_review = Review()
        objs.new(new_base)
        objs.new(new_user)
        objs.new(new_state)
        objs.new(new_place)
        objs.new(new_city)
        objs.new(new_amenity)
        objs.new(new_review)
        objs.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + new_base.id, save_text)
            self.assertIn("User." + new_user.id, save_text)
            self.assertIn("State." + new_state.id, save_text)
            self.assertIn("Place." + new_place.id, save_text)
            self.assertIn("City." + new_city.id, save_text)
            self.assertIn("Amenity." + new_amenity.id, save_text)
            self.assertIn("Review." + new_review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
