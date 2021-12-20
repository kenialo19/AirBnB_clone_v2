#!/usr/bin/python3
"""This module contains a class that inherits from BaseModel."""


from models.base_model import BaseModel


class User(BaseModel):
    """This class defines attributes of the user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes user."""
        super().__init__(*args, **kwargs)
