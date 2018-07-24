import sys
from os.path import join, dirname, abspath
import pytest

sys.path.append(join(abspath(dirname(__file__)), "../src"))

from rectangle import RectangleShape

class TestRectangle:
    @pytest.mark.parametrize("length, breath, result",
                             [
                                 (2, 3, 6),
                                 (4, 3, 12),
                                 (8, 8, 64)
                             ])
    def test_area_of_rectangle(self, length, breath, result):
        rectagle_shape = RectangleShape(length, breath)
        area_of_rectangle = rectagle_shape.get_area()

        assert area_of_rectangle == result

    @pytest.mark.parametrize("length, breath, result",
                             [
                                 (2, 3, 10),
                                 (4, 3, 14),
                                 (8, 8, 32)
                             ])
    def test_perimeter_of_rectangle(self, length, breath, result):
        rectagle_shape = RectangleShape(length, breath)
        peri_of_rectangle = rectagle_shape.get_perimeter()

        assert peri_of_rectangle == result


    @pytest.mark.parametrize("length, breath, result",
                             [
                                 (2, 13, 10),
                                 (4, 3, 14),
                                 (8, 8, 32)
                             ])
    @pytest.mark.skip(reason="Not Required for demo purpose")
    def test_perimeter_of_rectangle_d1(self, length, breath, result):
        rectagle_shape = RectangleShape(length, breath)
        peri_of_rectangle = rectagle_shape.get_perimeter()
        assert peri_of_rectangle == result


    @pytest.mark.parametrize("length, breath, result",
                             [
                                 (2, 13, 10),
                                 (4, 3, 14),
                                 (8, 8, 32)
                             ])
    @pytest.mark.skipif(sys.version_info < (3, 7), reason="Not Required for demo purpose")
    def test_perimeter_of_rectangle_d2(self, length, breath, result):
        rectagle_shape = RectangleShape(length, breath)
        peri_of_rectangle = rectagle_shape.get_perimeter()
        assert peri_of_rectangle == result