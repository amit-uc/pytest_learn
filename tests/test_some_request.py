import sys
from os.path import join, dirname, abspath

sys.path.append(join(abspath(dirname(__file__)), "../src"))
import pytest
from some_requests import dummy_call
from requests.models import Response

def test_sum(monkeypatch):
    #monkeypatch.setattr(Response, "content", "Hello world")
    data = dummy_call()

    assert data.content == "dada"
