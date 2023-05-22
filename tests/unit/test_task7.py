import pytest
from rosyk_task7 import Point, Vector


FIRST_VECTOR = Vector(Point(0, 0), Point(5, 8))
SECOND_VECTOR = Vector(Point(9, 1), Point(6, 3))
ZERO_VECTOR = Vector(Point(0, 0), Point(0, 0))


def test_vector_init():
    vector = FIRST_VECTOR
    assert vector.length == pytest.approx(9.433, 0.001)
    assert vector.x == 5
    assert vector.y == 8


@pytest.mark.parametrize('vector1, vector2, expected',
                         [(FIRST_VECTOR, SECOND_VECTOR,
                           {'x': 2, 'y': 10}),
                          (ZERO_VECTOR, ZERO_VECTOR,
                           {'x': 0, 'y': 0})])
def test_vector_addition(vector1, vector2, expected):
    result = vector1 + vector2
    assert result.x == expected['x']
    assert result.y == expected['y']


@pytest.mark.parametrize('vector1, vector2, expected_x, expected_y',
                         [(FIRST_VECTOR, SECOND_VECTOR, 8, 6),
                          (ZERO_VECTOR, ZERO_VECTOR, 0, 0)])
def test_vector_subtraction(vector1, vector2, expected_x, expected_y):
    result = vector1 - vector2
    assert result.x == expected_x
    assert result.y == expected_y
