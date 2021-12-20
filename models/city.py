#!/usr/bin/python3
"""This module contains a class that inherits from BaseModel."""


from models.base_model import BaseModel


class City(BaseModel):
    """This class defines the city."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state."""
        super().__init__(*args, **kwargs)
