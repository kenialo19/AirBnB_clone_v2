#!/usr/bin/python3
"""Unittest for State module."""
import unittest
from models.state import State
from models.base_model import BaseModel
import os


class TestPlace(unittest.TestCase):
    """This class tests state module."""

    def setUp(self):
        """Sets up the testing environment"""

        self.state_1 = State()
        self.state_2 = State()
        self.state_2.name = "Risaralda"
        self.state_2.name = "Antioquia"

    def tearDown(self):
        """Tears down the testing environment."""

        del self.state_1
        del self.state_2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_instance(self):
        """Checks that new instance was created."""

        self.assertTrue(self.state_1)
        self.assertTrue(self.state_2)

    def test_inheritance(self):
        """Review inherits from BaseModel."""

        self.assertTrue(issubclass(State, BaseModel))

    def test_attr(self):
        """Checks that new instance has attributes."""

        self.assertIn("name", self.state_2.__dict__)
        self.assertEqual(self.state_2.name, "Antioquia")
