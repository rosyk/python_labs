import pytest
import numpy as np
from rosyk_task5 import row_sum, numbers_amount, geron_sqrt


@pytest.mark.parametrize('input_param, expected', [(0.001, 0)])
def test_row_sum(input_param, expected):
    assert row_sum(input_param) == expected


@pytest.mark.parametrize('input_param, expected', [(12345, 5)])
def test_numbers_amount(input_param, expected):
    assert numbers_amount(input_param) == expected


@pytest.mark.parametrize('input_param, eps, expected', [(25, 0.001, 0)])
def test_geron_sqrt(input_param, eps, expected):
    assert abs(geron_sqrt(input_param, eps) - np.sqrt(input_param)) <= eps
