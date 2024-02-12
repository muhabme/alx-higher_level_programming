#!/usr/bin/python3

"""Defines a base model class."""

class Base:
    """Base model.

    This Represents the base for all other classes in project "Python - Almost a Circle"*.

    Private Class Attributes:
        __nb_object (int): num of instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init a new Base.

        Args:
            id (int): id of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
