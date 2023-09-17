#!/usr/bin/python3
"""This defines the class called User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email : Email of the user.
        password : Password of the user.
        first_name : First name of the user.
        last_name : Last name of user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
