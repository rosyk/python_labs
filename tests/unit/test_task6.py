import pytest
from task6.rosyk_task6 import numbers_sum


def test_numbers_sum():
    result = numbers_sum()
    assert result == '45'
