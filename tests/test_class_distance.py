import sys
from os.path import join, dirname, abspath
import pytest

sys.path.append(join(abspath(dirname(__file__)), "../src"))

from Distance import Distance
from Distance import Point

class TestRectangle:
    @pytest.mark.parametrize("point_1, point_2, distance",
                             [
                                 (Point(13, 7), Point(9, 4), 5),
                             ])
    def test_distance(self, point_1, point_2, distance, monkeypatch):
        def dummy():
            return ""
        # monkeypatch.setattr(Distance, "_calculate_distance", lambda x: None)
        dist = Distance(point_1, point_2)

        assert (dist.distance == distance)

