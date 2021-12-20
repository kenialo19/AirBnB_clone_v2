#!/usr/bin/python3
"""""""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models

class test_storage(unittest.TestCase):
    """"""
    def test_path_atribute(self):
        """"""
        self.assertTrue(FileStorage._FileStorage_file_path, "file.json")
        self.assertEqual(FileStorage._FileStorage_file_path != 0)
        self.assertTrue(type(FileStorage._FileStorage_file_path) is str)
    
    def test_class_obj(self):
        """"""
        self.assertTrue(type(FileStorage._FileStorage_objects) is dict)
    
    def test_all(self):
        """"""
        object = models.storage.all()
        self.assertIsInstance(object, dict)

    def test_save(self):
        """"""
        pass

    def test_reload(self):
        """"""
        pass
    


    
