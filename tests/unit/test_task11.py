from unittest.mock import mock_open
import pytest
from rosyk_task11 import find_student_phone, create_letter, create_dict, create_years_dict


@pytest.mark.parametrize('input_param, expected', [('str+380991234567str', '+380991234567'),
                                                   ('str380991234567str', '+380991234567'),
                                                   ('str0991234567str', '+380991234567')])
def test_find_student_phone(input_param, expected):
    assert find_student_phone(input_param) == expected


@pytest.mark.parametrize('input_param, expected',
                         [('адр вул. Лесі Українки, 13 кв 56 Симоненко В. К. тел 380991234567 10000',
                          ('тел 380991234567, адр вул. Лесі Українки, 13 кв 56\n'
                           'Dear Симоненко В. К.\nThe amount of your debt for services is 10000.\n'
                           'Please pay the debt within a month. '
                           'Otherwise, the provision of services will be discontinued.\n\n',))])
def test_create_letter(input_param, expected, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    create_letter()
    print(open.mock_calls[5][1])
    assert open.mock_calls[5][1] == expected


@pytest.mark.parametrize('input_param, expected',
                         [('Михайличенко Андрій Степанович 12345 01.01.2000 +380991234567',
                           {'12345': 'Михайличенко Андрій Степанович, 01.01.2000, +380991234567'})])
def test_create_dict(input_param, expected, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    assert create_dict() == expected


@pytest.mark.parametrize('input_param, expected', [('year 2023', {'2023': 0}), ('', {})])
def test_create_years_dict(input_param, expected, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    assert create_years_dict() == expected
