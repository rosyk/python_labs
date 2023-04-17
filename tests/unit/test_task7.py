import pytest
from rosyk_task7 import Point, Vector


def test_vector_init():
    vector = Vector(Point(0, 0), Point(5, 8))
    assert vector.length == pytest.approx(9.433, 0.001)
    assert vector.x == 5
    assert vector.y == 8


@pytest.fixture()
def first_vector():
    return Vector(Point(0, 0), Point(5, 8))


@pytest.fixture()
def second_vector():
    return Vector(Point(9, 1), Point(6, 3))


@pytest.fixture()
def zero_vector():
    return Vector(Point(0, 0), Point(0, 0))


@pytest.mark.parametrize('vectors, expected',
                         [(['first_vector', 'second_vector'],
                           {'x': 2, 'y': 10}),
                          (['zero_vector', 'zero_vector'],
                           {'x': 0, 'y': 0})])
def test_vector_addition(vectors, expected, request):
    first_vector = request.getfixturevalue(vectors[0])
    second_vector = request.getfixturevalue(vectors[1])

    result = first_vector + second_vector
    assert result.x == expected['x']
    assert result.y == expected['y']


@pytest.mark.parametrize('vectors, expected',
                         [(['first_vector', 'second_vector'],
                           {'x': 8, 'y': 6}),
                          (['zero_vector', 'zero_vector'],
                           {'x': 0, 'y': 0})])
def test_vector_subtraction(vectors, expected, request):
    first_vector = request.getfixturevalue(vectors[0])
    second_vector = request.getfixturevalue(vectors[1])

    result = first_vector - second_vector
    assert result.x == expected['x']
    assert result.y == expected['y']
