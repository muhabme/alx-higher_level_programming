#!/usr/bin/python3
"""Defines a square class."""

# Importing the Rectangle class from models package
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class inherits from Rectangle and represents a square shape.
    
    Attributes:
        size (int): Dimension of the square's sides.
        x (int): Horizontal position.
        y (int): Vertical position.
        id (int): Unique identifier.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance with size, position, and an optional id.
        
        Args:
            size (int): The length of the square's sides.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): An identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)  # Call to the superclass constructor

    @property
    def size(self):
        """Property getter for the size of the square."""
        return self.width  # Width and height are the same for a square

    @size.setter
    def size(self, value):
        """
        Property setter for the size of the square, updating both width and height.
        
        Args:
            value (int): The new size for the square's sides.
        """
        self.width = self.height = value  # Set both width and height to the new size

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes with either args or kwargs, if present.
        
        Args:
            *args (int): Non-keyword arguments for id, size, x, and y in order.
            **kwargs (dict): Keyword arguments specifying new values for attributes.
        """
        # Update with args if present
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for index, value in enumerate(args):
                setattr(self, attributes[index], value) if index < len(attributes) else None

        # Alternatively, update with kwargs if args are not provided
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the square instance into a dictionary representation.
        
        Returns:
            dict: A dictionary with the square's id, size, x, and y.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """
        Defines the string representation of the square.
        
        Returns:
            str: A string describing the square with its id, position, and size.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
