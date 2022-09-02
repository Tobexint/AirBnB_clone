#!/usr/bin/python3
"""Defines unittests for models/base_.model.py"""
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="777", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "777")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))


if __name__ == "__main__":
    unittest.main()
