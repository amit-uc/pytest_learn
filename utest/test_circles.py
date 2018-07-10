import sys
from os.path import join, dirname, abspath
import unittest

sys.path.append(join(abspath(dirname(__file__)), "../src"))

from circles import area_of_circle
from math import pi

class CircleTestCase(unittest.TestCase):
    def setUp(self):
        self.num = 2

    def test_one(self):
        self.num = 4
        self.assertEqual(self.num, 4)

    def test_two(self):
        self.assertEqual(self.num, 4)

    def test_area(self):
        assert area_of_circle(0) == 0
        assert area_of_circle(1) == pi
        assert area_of_circle(2.4) == pi * 2.4**2