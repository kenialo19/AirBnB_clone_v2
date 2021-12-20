#!/usr/bin/python3
"""test module for the user class"""


import unittest
from models.user import User
from models.base_model import BaseModel
import os


class test_user(unittest.TestCase):
    """test the user class"""

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

    def test_instantiation(self):
        """"test if user subclass basemodel"""
        user_1 = User()
        self.assertEqual(str(type(user_1)), "<class 'models.user.user'>")
        self.assertIsInstance(user_1, User)
        self.assertTrue(issubclass(type(user_1), BaseModel))

    def test_atributes(self):
        """test atributte type user"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(type(self.user, "name"), True)
