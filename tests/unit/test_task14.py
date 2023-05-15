from copy import deepcopy
from unittest.mock import patch
import pytest
from rosyk_task14 import Multiset, exel_weather

MULTISET = Multiset({1: 2})
EMPTY_MULTISET = Multiset()


@pytest.mark.parametrize('input_param, expected', [(deepcopy(MULTISET), None)])
def test_clear(input_param, expected):
    assert input_param.clear() == expected


@pytest.mark.parametrize('input_param, expected', [(MULTISET, False), (deepcopy(EMPTY_MULTISET), True)])
def test_is_empty(input_param, expected):
    assert input_param.is_empty() == expected


@pytest.mark.parametrize('input_param, expected', [(deepcopy(EMPTY_MULTISET), '{1: 1}'),
                                                   (deepcopy(MULTISET), '{1: 3}')])
def test_add(input_param, expected):
    input_param.add(1)
    assert str(input_param) == expected


@pytest.mark.parametrize('input_param, expected', [(deepcopy(MULTISET), '{1: 1}')])
def test_remove(input_param, expected):
    input_param.remove(1)
    assert str(input_param) == expected


def test_remove_error():
    with pytest.raises(ValueError):
        deepcopy(EMPTY_MULTISET).remove(1)


@pytest.mark.parametrize('input_param, expected', [(Multiset({1: 2}), 2), (Multiset(), 0)])
def test_count(input_param, expected):
    assert input_param.count(1) == expected


@pytest.mark.parametrize('input_param, expected', [(deepcopy(MULTISET), '{1: 3}'), (Multiset({1: 4}), '{1: 4}')])
def test_union(input_param, expected):
    assert str(input_param.union(Multiset({1: 3}))) == expected


@pytest.mark.parametrize('input_param, expected', [(deepcopy(MULTISET), '{1: 2}'), (Multiset({1: 4}), '{1: 3}')])
def test_intersrction(input_param, expected):
    assert str(input_param.intersection(Multiset({1: 3}))) == expected


def test_exel_weather():
    with patch('rosyk_task14.Workbook') as mock_wb, patch('rosyk_task14.requests.get') as mock_get:
        html_content = """
                    <html>
                        <body>
                            <div class="main">
                                <div class="temperature">
                                    <div class="min">мин. 12</div>
                                    <div class="max">макс. 20</div>
                                </div>
                            </div>
                        </body>
                    </html>
                """
        mock_get.return_value.content = html_content.encode('utf-8')
        exel_weather('киев')
        assert mock_wb.mock_calls[2][1] == (['2023-05-15', '20', '12'],)
