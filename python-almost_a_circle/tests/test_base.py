#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Testing the Base Class"""

    def setUp(self):
        """imports the variable"""
        Base.__nb_objects = 0
        pass

    def tearDown(self):
        """Clean up code"""
        pass

    def test_A_nb_objects_private(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
