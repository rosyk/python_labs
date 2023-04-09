import pytest
from unittest.mock import patch
from rosyk_task8_9 import site_users_greeting, figure_name, ordinals, odd_even, number_of_days, ordinary_leap_year, \
    numbers_sum, calculator, person_on_money, cell_color, decimal_to_binary, rock_paper_scissors


@pytest.mark.parametrize('input_param, expected', [([], 'We need to find some users'),
                                                   (['Admin', 'Alex'],
                                                    'Hello, Admin, I hope you`re doing well'
                                                    '\nHello, Alex, thank you for logging in again')])
def test_site_users_greeting_no_users(input_param, expected, capsys):
    site_users_greeting(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [(0, 'the number of sides is less than 3 or more than 6'),
                                                   (3, 'it`s triangle'),
                                                   (4, 'it`s rectangle'),
                                                   (5, 'it`s pentagon'),
                                                   (6, 'it`s hexagon'),
                                                   (7, 'the number of sides is less than 3 or more than 6')])
def test_figure_name(input_param, expected, capsys):
    figure_name(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [([1, 2, 3, 4], '1st\n2nd\n3rd\n4th')])
def test_ordinals(input_param, expected, capsys):
    ordinals(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# @patch('builtins.input', return_value=1)
# def test_odd_even(capsys):
#     odd_even()
#     captured = capsys.readouterr()
#     assert captured.out.strip() == '1 is odd'
#
#
# def test_number_of_days():
#     number_of_days()


@pytest.mark.parametrize('input_param, expected', [(2000, 'leap year'), (2001, 'ordinary year')])
def test_ordinary_leap_year(input_param, expected, capsys):
    ordinary_leap_year(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# def test_numbers_sum():
#     numbers_sum()
#
#
# def test_calculator():
#     calculator()


@pytest.mark.parametrize('input_param, expected', [(1, '1 - Volodymyr Velykiy'), (2, '2 - Yaroslav Mydriy'), (5, '5 - Bohdan Hmelnitsky'),
                                                   (10, '10 - Ivan Mazepa'), (20, '20 - Ivan Franko'), (50, '50 - Myhaylo Hrushevsky'),
                                                   (100, '100 - Taras Shevchenko'), (200, '200 - Lesya Ukrainka'), (500, '500 - Grigory Skovoroda'),
                                                   (1000, '1000 - Volodymyr Vernadsky'), (3, 'nominal doesn`t exist')])
def test_persons_on_money(input_param, expected, capsys):
    person_on_money(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# def test_cell_color():
#     cell_color()


@pytest.mark.parametrize('input_param, expected', [(10, '10 is 1010\n1010 is 10'), (135, '135 is 10000111\n10000111 is 135')])
def test_decimal_to_binary(input_param, expected, capsys):
    decimal_to_binary(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected