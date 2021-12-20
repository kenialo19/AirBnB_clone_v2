#!/usr/bin/python3
"""Test BaseModel for expected behavior and cocumentation."""
import models
import unittest
import os
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """Unit test for the BaseModel class."""

    def setUp(self):
        """Sets up testing environment."""
        self.model = BaseModel()
        self.model_1 = BaseModel()

    def tearDown(self):
        """Breaks down thes test."""
        del self.model
        del self.model_1
        if os.path.exists("file.json"):
            os.remove()

    def test_id(self):
        """check if the id of two instances is different"""
        model = BaseModel()
        model_1 = BaseModel()
        self.assertNotEqual(model.id, model_1.id)

    def test_save(self):
        """check if the updated_at attribute (date) is updated
        for the same object with the current date. the same object
        with the current date"""
        model_2 = BaseModel()
        update_1 = model_2.updated_at
        model_2.save()
        update_2 = model_2.updated_at
        self.assertNotEqual(update_1, update_2)

    def test_to_dict(self):
        """check if to_dict returns a dictionary, if it adds a class with the object's
        class name, and if updated_at and updated_at return a dictionary.
        with the object's class name, and if updated_at and
        created_at are converted to string object in ISO format."""
        model_3 = BaseModel()
        dict_model = model_3.to_dict()
        self.assertIsInstance(dict_model, dict)
        for key, value in dict_model.items():
            flag = 0
            if dict_model["__class__"] == "BaseModel":
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in dict_model.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)

    def test_save(self):
        """Tests if info has been saved to file."""
        model_2 = BaseModel()
        model_2.save()
        with open("file.json", "r") as f:
            self.assertIn(model_2.id, f.read())

if __name__ == '__main__':
    unittest.main()
