import pytest
from main import sum_two_integers


def test_sum_two_integers_positive():
    assert sum_two_integers(3, 5) == 8


def test_sum_two_integers_negative():
    assert sum_two_integers(-2, -4) == -6


def test_sum_two_integers_mixed():
    assert sum_two_integers(-1, 1) == 0


def test_sum_two_integers_zero():
    assert sum_two_integers(0, 0) == 0
