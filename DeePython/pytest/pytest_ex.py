import pytest


class Bottle:

    @property
    def water(self):
        return 10


def test_check_water():
    bottle = Bottle()
    assert 10 == bottle.water


def test_wail_fail():
    pytest.fail("WILL FAIL")
