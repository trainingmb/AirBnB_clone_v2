#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

storage_t = os.environ.get("HBNB_TYPE_STORAGE","")
storage = ""
if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
