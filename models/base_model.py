#!/usr/bin/python3
"""Defines the BaseModel class."""
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods"""

    def __init__(self, *args, **kwargs):
        """Initializes all attributes"""

        tf = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tf)
                else:
                    self.__dict__[key] = value
        else:
            storage.new(self)

    def __str__(self):
        """Returns the class name, id and attribute dictionary"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
