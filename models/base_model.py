#!/usr/bin/python3
"""
Module for BaseModel class.
"""
from datetime import datetime
import uuid

class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.

    Public instance attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Date and time when the instance is created.
        updated_at (datetime): Date and time when the instance is last updated.

    Public instance methods:
        __init__(self, *args, **kwargs): Initializes a new instance of the BaseModel class.
        __str__(): Returns a string representation of the instance.
        save(self): Updates the 'updated_at' attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Unused.
            **kwargs: Dictionary of attributes for creating the instance.
        """
        # Your initialization code here
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        from models import storage  # Import 'storage' here to avoid circular imports
        self.updated_at = datetime.now()
        storage.save()  # Call storage.save to save changes to the file

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

# Test the BaseModel class
if __name__ == "__main__":
    pass
