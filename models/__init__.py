#!/usr/bin/python3
"""
This module initializes the models package.
"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Call the reload() method on this variable
storage.reload()
