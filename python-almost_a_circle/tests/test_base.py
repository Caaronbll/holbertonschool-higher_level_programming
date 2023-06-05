#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Testing the Base Class"""

    def setUp(self):
        Base.__nb_objects = 0
        pass
