import sys
from os.path import join, dirname, abspath
from datetime import datetime
sys.path.append(join(abspath(dirname(__file__)), "../src"))
import pytest
from dummy_file import Dummy
from unittest import mock
#
# @pytest.fixture
# def patch_datetime_now(monkeypatch):
#
#     class CustomDatetime:
#         @classmethod
#         def now(cls):
#             return "2018-07-14_18:48:43.412671"
#
#     monkeypatch.setattr(datetime, 'datetime', CustomDatetime)
#

def okay(dummy, a, b):
    return f"{a}/{b}-ada"

def test_dummy(monkeypatch):
    monkeypatch.setattr(Dummy, "okay", okay)
    dum = Dummy()

    assert (dum.okay(1, 2) == "1/2-ada")


def test_get_da(monkeypatch):
    dum = Dummy()
    dum.__test = 4
    #monkeypatch.setattr(dum, "__test", 4)
    assert(dum.get_test() == 2)

# @mock.patch('dummy_file.datetime.now')
# def test_datetime(now_mock):
#
#     valid_datetime = "2018-07-14_18:48:43.412671"
#     now_mock.return_value = datetime.now()
#
#
#
#     dum = Dummy()
#
#     assert (dum.get_time() == valid_datetime)
#

def test_pk_test(monkeypatch):
    monkeypatch.setattr(Dummy, "test", 23)

    dum = Dummy

    assert (dum.test == 23)
#
@mock.patch('dummy_file.datetime.now')
def test_datetime(monkeypatch):

    monkeypatch.setattr(datetime, "_datetime_now", lambda x: datetime(2018, 7, 17, 14, 20, 20, 178432))
    valid_datetime = "2018-07-17 14:20:20.178432"

    #now_mock.return_value = datetime.now()



    dum = Dummy()

    assert (dum.get_time() == valid_datetime)