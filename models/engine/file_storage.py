#!/usr/bin/python3
"""
Module for FileStorage class.
"""
import json
import os
from models.base_model import BaseModel

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
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_data = value
                    class_ = eval(class_name)
                    new_obj = class_(**obj_data)
                    self.__objects[key] = new_obj
