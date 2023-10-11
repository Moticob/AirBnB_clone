#!/usr/bin/python3
"""
This is a test script for the BaseModel class in the AirBnB project.
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str(self):
        model = BaseModel()
        string = model.__str__()
        self.assertEqual(string, "[BaseModel] ({}) {}".format(model.id, model.__dict__))

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue("__class__" in model_dict)
        self.assertTrue("created_at" in model_dict)
        self.assertTrue("updated_at" in model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

    def test_create_instance_from_dict(self):
        model = BaseModel()
        model_json = model.to_dict()
        new_model = BaseModel(**model_json)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)

if __name__ == "__main__":
    unittest.main()

