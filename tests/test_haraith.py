import sys
from os.path import join, dirname, abspath

sys.path.append(join(abspath(dirname(__file__)), "../src"))
import pytest
from sum import sumd
import sum

class NumberSumd:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_sum(self):
        return self.__a - self.__b


# @mock.patch("__main__.okay", side_effect=lambda x,y: 0)
@pytest.mark.parametrize("a", [1])
@pytest.mark.parametrize("b", [4, 5, 6])
def test_sum(a, b, monkeypatch):
    monkeypatch.setattr(sum, "okay", lambda x,y: NumberSumd(x,y))
    da = sumd(a, b)
    print(da.get_sum())
    assert da.get_sum() == (a-b)

