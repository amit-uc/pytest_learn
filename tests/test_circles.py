import sys
from os.path import join, dirname, abspath

sys.path.append(join(abspath(dirname(__file__)), "../src"))

from circles import area_of_circle
from math import pi

def test_area():
    assert area_of_circle(0) == 0
    assert area_of_circle(1) == pi
    assert area_of_circle(2.4) == pi * 2.4**2