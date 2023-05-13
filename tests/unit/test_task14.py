import pytest
from unittest.mock import patch
from rosyk_task14 import Multiset

MULTISET = Multiset({1: 2})
EMPTY_MULTISET = Multiset()


@pytest.mark.parametrize('input_param, expected', [(Multiset({1: 2}), None)])
def test_clear(input_param, expected):
    assert input_param.clear() == expected


@pytest.mark.parametrize('input_param, expected', [(Multiset({1: 2}), False), (Multiset(), True)])
def test_is_empty(input_param, expected):
    assert input_param.is_empty() == expected


@pytest.mark.parametrize('input_param, expected', [(Multiset(), '{1: 1}'), (Multiset({1: 2}), '{1: 3}')])
def test_add(input_param, expected):
    input_param.add(1)
    assert str(input_param) == expected


@pytest.mark.parametrize('input_param, expected', [(Multiset({1: 2}), '{1: 1}')])
def test_remove(input_param, expected):
    input_param.remove(1)
    assert str(input_param) == expected


@pytest.mark.parametrize('input_param, expected', [(Multiset({1: 2}), 2), (Multiset(), 0)])
def test_count(input_param, expected):
    assert input_param.count(1) == expected


@pytest.mark.parametrize('input_param, expected', [(Multiset({1: 2}), '{1: 3}'), (Multiset({1: 4}), '{1: 4}')])
def test_union(input_param, expected):
    assert str(input_param.union(Multiset({1: 3}))) == expected

@pytest.mark.parametrize('input_param, expected', [(Multiset({1: 2}), '{1: 2}'), (Multiset({1: 4}), '{1: 3}')])
def test_intersrction(input_param, expected):
    assert str(input_param.intersection(Multiset({1: 3}))) == expected

def test_exel_weather():

