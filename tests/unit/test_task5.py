import pytest
import numpy as np
from rosyk_task5 import row_sum, numbers_amount, geron_sqrt


@pytest.mark.parametrize('input_param, expected', [(0.001, 0)])
def test_row_sum(input_param, expected):
    assert row_sum(input_param) == expected


@pytest.mark.parametrize('input_param, error', [(0, pytest.raises(ZeroDivisionError)), ('string', pytest.raises(TypeError)), (-1, pytest.raises(ZeroDivisionError))])
def test_row_sum_errors(input_param, error):
    with error:
        row_sum(input_param)

@pytest.mark.parametrize('input_param, expected', [(12345, 5), (123, 3), (0, 1), (-1, 1)])
def test_numbers_amount(input_param, expected):
    assert numbers_amount(input_param) == expected


def test_numbers_amount_error():
    with pytest.raises(TypeError):
        numbers_amount('string')


@pytest.mark.parametrize('input_param, eps', [(25, 0.001), (0, 0.001)])
def test_geron_sqrt(input_param, eps):
    assert abs(geron_sqrt(input_param, eps) - np.sqrt(input_param)) <= eps


@pytest.mark.parametrize('input_param, error', [(-1, pytest.raises(ValueError)), ('string', pytest.raises(TypeError))])
def test_geron_sqrt_errors(input_param, error):
    with error:
        geron_sqrt(input_param, 0.001)
