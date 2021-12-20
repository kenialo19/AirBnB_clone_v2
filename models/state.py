#!/usr/bin/python3
"""This module contains a class that inherits from BaseModel."""

from models.base_model import BaseModel


class State(BaseModel):
    """This class represents the state."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state."""
        super().__init__(*args, **kwargs)
