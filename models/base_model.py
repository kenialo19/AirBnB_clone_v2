#!/usr/bin/python3
"""This module contains the parent class: BaseModel."""


import uuid
from datetime import datetime
import models


date_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Parent class which defines all common attributes or
    methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes."
        where *args won’t be used, kwargs is not empty, otherwise
        create id and created_at (new instance)"""

        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, date_time)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, date_time)
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints representation of the BaseModel class."""

        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute with the current datetime."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict. containing all keys/values of the instance."""

        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic
