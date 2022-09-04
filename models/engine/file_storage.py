#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name >.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            jsn_file = json.dump(dict, f)

    def reload(self):
        """  deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists """
        try:
            with open(FileStorage.__file_path) as f:
                jsn_file = json.load(f)
        except FileNotFoundError:
            pass
