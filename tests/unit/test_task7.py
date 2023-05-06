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




@pytest.mark.parametrize('vectors, expected',
                         [([FIRST_VECTOR, SECOND_VECTOR],
                           {'x': 2, 'y': 10}),
                          ([ZERO_VECTOR, ZERO_VECTOR],
                           {'x': 0, 'y': 0})])
def test_vector_addition(vectors, expected):
    result = vectors[0] + vectors[1]
    assert result.x == expected['x']
    assert result.y == expected['y']


@pytest.mark.parametrize('vectors, expected',
                         [([FIRST_VECTOR, SECOND_VECTOR],
                           {'x': 8, 'y': 6}),
                          ([ZERO_VECTOR, ZERO_VECTOR],
                           {'x': 0, 'y': 0})])
def test_vector_subtraction(vectors, expected):
    result = vectors[0] - vectors[1]
    print(result.x, result.y)
    assert result.x == expected['x']
    assert result.y == expected['y']
