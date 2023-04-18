from unittest.mock import patch

import pytest

from rosyk_task8_9 import site_users_greeting, figure_name, ordinals, odd_even, number_of_days,\
    ordinary_leap_year, numbers_sum, calculator, person_on_money, cell_color,\
    decimal_to_binary, rock_paper_scissors


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


@pytest.mark.parametrize('input_param, expected', [(1, '1 is odd'), (2, '2 is even'),
                                                   (0, '0 is even'), (-1, '-1 is odd')])
def test_odd_even(input_param, expected, capsys):
    with patch('utils.number_validation_input', return_value=input_param):
        odd_even()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected


#
#
@pytest.mark.parametrize('input_param, expected',
                         [('january', 'in January 31 days'), ('string', 'month doesn`t exist')])
def test_number_of_days(input_param, expected, capsys):
    with patch('builtins.input', return_value=input_param):
        number_of_days()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [(2000, 'leap year'), (2001, 'ordinary year')])
def test_ordinary_leap_year(input_param, expected, capsys):
    ordinary_leap_year(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [([1, 2, 0], '3'), ([-1, 1, 0], '0'), ([0], '0')])
def test_numbers_sum(input_param, expected, capsys):
    with patch('utils.number_validation_input', side_effect=input_param):
        numbers_sum()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected


@pytest.mark.parametrize('numbers, operator, expected', [([2, 3], '+', '5'), ([2, 1], '-', '1'),
                                                         ([6, 3], '/', '2.0'), ([5, 5], '*', '25'),
                                                         ([10, 3], 'mod', '1'), ([3, 2], 'pow', '9'),
                                                         ([10, 3], 'div', '3')])
def test_calculator(numbers, operator, expected, capsys):
    with patch('utils.number_validation_input', side_effect=numbers), \
            patch('builtins.input', return_value=operator):
        calculator()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [(1, '1 - Volodymyr Velykiy'), (2, '2 - Yaroslav Mydriy'),
                                                   (5, '5 - Bohdan Hmelnitsky'), (10, '10 - Ivan Mazepa'),
                                                   (20, '20 - Ivan Franko'), (50, '50 - Myhaylo Hrushevsky'),
                                                   (100, '100 - Taras Shevchenko'), (200, '200 - Lesya Ukrainka'),
                                                   (500, '500 - Grigory Skovoroda'),
                                                   (1000, '1000 - Volodymyr Vernadsky'),
                                                   (3, 'nominal doesn`t exist')])
def test_persons_on_money(input_param, expected, capsys):
    person_on_money(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [('a1', 'cell is black'),
                                                   ('a2', 'cell is white'),
                                                   ('string', 'incorrect cell')])
def test_cell_color(input_param, expected, capsys):
    with patch('builtins.input', return_value=input_param):
        cell_color()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [(10, '10 is 1010\n1010 is 10'),
                                                   (135, '135 is 10000111\n10000111 is 135')])
def test_decimal_to_binary(input_param, expected, capsys):
    decimal_to_binary(input_param)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, computer_choise, expected',
                         [(['paper', 'n'], 'rock', 'you choose paper, computer choose rock...\nyou win!'),
                          (['paper', 'n'], 'scissors', 'you choose paper, computer choose scissors...\nyou lose!'),
                          (['paper', 'n'], 'paper', 'you choose paper, computer choose paper...\ndraw!')])
def test_rock_paper_scissors(input_param, computer_choise, expected, capsys):
    with patch('random.choice', return_value=computer_choise), patch('builtins.input', side_effect=input_param):
        rock_paper_scissors()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected
