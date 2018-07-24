import sys
from os.path import join, dirname, abspath

sys.path.append(join(abspath(dirname(__file__)), "../src"))
import pytest
from sum import sum

@pytest.mark.parametrize("a", [1])
@pytest.mark.parametrize("b", [4, 5])
def test_sum(a, b):
    print(a, b)
    assert sum(a, b) == (a+b)

