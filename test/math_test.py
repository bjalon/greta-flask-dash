import pytest

from service.math import subtract


def test_should_return_one_when_subtract_two_and_one():
    assert subtract(2, 1) == 1


def test_should_return__when_subtract_three_and_one():
    assert subtract(3, 1) == 2
