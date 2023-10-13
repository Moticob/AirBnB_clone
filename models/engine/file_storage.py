#!/usr/bin/python3
"""
Module for FileStorage class.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    FileStorage class for serializing and deserializing instances to/from a JSON file.

    Private class attributes:
        __file_path (str): Path to the JSON file (ex: file.json).
        __objects (dict): Dictionary to store all objects by <class name>.id.

    Public instance methods:
        all(self): returns the dictionary __objects.
        new(self, obj): sets in __objects the obj with key <obj class name>.id.
        save(self): serializes __objects to the JSON file (path: __file_path).
        reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: A dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
        """
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)

            for obj_id, obj_data in data.items():
                obj_class = obj_data.get('__class')
                if obj_class == 'BaseModel':
                    obj = BaseModel(**obj_data)
                elif obj_class == 'User':
                    obj = User(**obj_data)
                # Add other classes here if needed

                self.__objects[obj_id] = obj
        except Exception:
            pass
