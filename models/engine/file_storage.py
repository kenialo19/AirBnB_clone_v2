#!/usr/bin/python3
"""This module contains a class that stores information
about instances."""


import json
from os import path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        __objects' values will be store like a dict by to_dict method."""

        jsonFile = {}
        for key, value in self.__objects.items():
            jsonFile[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(jsonFile, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing."""

        ddict = {}
        classList = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                     "Place": Place, "Review": Review, "State": State,
                     "User": User}

        try:
            d = {}
            with open(self.__file_path, encoding='utf-8') as f:
                ddict = json.load(f)
            for key, value in ddict.items():
                if value["__class__"] in classList:
                    d = classList[value["__class__"]](**value)
                    self.__objects[key] = d
        except Exception:
            pass
