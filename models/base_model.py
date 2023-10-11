#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.

    Public instance attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Date and time when the instance is created.
        updated_at (datetime): Date and time when the instance is last updated.

    Public instance methods:
        __str__(): Returns a string representation of the instance.
        save(): Updates the 'updated_at' attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance.
    """
    def __init__(self):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

if __name__ == '__main__':
    pass

