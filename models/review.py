#!/usr/bin/python3
"""This defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This represents  a review."""

    place_id = ""
    user_id = ""
    text = ""
