import pytest
from main import sum_two_integers


def test_sum_two_integers_positive():
    assert sum_two_integers(3, 5) == 8
