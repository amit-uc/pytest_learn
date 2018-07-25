import pytest
import sys
from os.path import join, dirname, abspath

sys.path.append(join(abspath(dirname(__file__)), "../src"))
import pytest
from sum import sumd
import sum


class SomeConnection:
    def execute_select_query(self, query, sql_args):
        if query == 1:
            return "Yo You are Hero"
        elif query == 2:
            return "Yo You are Zero"

        return "Yo You are Vineet"

def other(x, y):
    return SomeConnection()

def test_some_connection(monkeypatch):
    monkeypatch.setattr(sum, "okay", other)

    da = sumd(1, 2)

    assert da.execute_select_query(1, 2) == "Yo You are Hero"


