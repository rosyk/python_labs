from unittest.mock import patch, mock_open
from io import StringIO
import pytest
from task6.rosyk_task6 import numbers_sum, odd_even_write, python_posibilities_print, python_change, \
    guests_greeting, the_counter, text_format, chapters_write, small_big_letters


@pytest.mark.parametrize('input_param, expected', [('1\n2\n3', ('6.0',))])
def test_find_sum_numbers(input_param, expected):
    with patch('builtins.open', mock_open(read_data=input_param)):
        numbers_sum()
        assert open.mock_calls[5][1] == expected


@pytest.mark.parametrize('input_param, expected', [('string', 'file contains something except numbers')])
def test_find_sum_number_string(input_param, expected, capsys):
    with patch('builtins.open', mock_open(read_data=input_param)):
        numbers_sum()
        captured = capsys.readouterr()
        assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [(2, ('2 is even',)), (3, ('3 is odd',))])
def test_odd_even_write(input_param, expected):
    with patch('sys.stdin', StringIO(str(input_param))):
        with patch('builtins.open', mock_open(read_data='')):
            odd_even_write()
            assert open.mock_calls[2][1] == expected


@pytest.mark.parametrize('input_param, expected', [('in python you can all', 'in python you can all')])
def test_python_posibilities_print(input_param, expected, monkeypatch, capsys):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    python_posibilities_print()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [('in Python you can all', 'in C you can all'),
                                                   ('without', 'without')])
def test_python_change(input_param, expected, monkeypatch, capsys):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    python_change()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [(['Alex', 'exit'], 'Welcome, Alex. Have a nice day!'),
                                                   (['Alex', 'John', 'exit'],
                                                    'Welcome, Alex. Have a nice day!\n'
                                                    'Welcome, John. Have a nice day!')])
def test_guests_greeting(input_param, expected, capsys):
    with patch('builtins.input', side_effect=input_param):
        with patch('builtins.open', mock_open(read_data='')):
            guests_greeting()
            captured = capsys.readouterr()
            assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [('text with the', '1'),
                                                   ('text without', '0')])
def test_the_counter(input_param, expected, capsys, monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    the_counter()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [('two\nlines', ('two lines',))])
def test_text_format(input_param, expected):
    with patch('builtins.open', mock_open(read_data=input_param)):
        text_format()
        print(open.mock_calls)
        assert open.mock_calls[5][1] == expected


@pytest.mark.parametrize('input_param, expected', [('CHAPTER 1', (['CHAPTER 1'],)),
                                                   ('', ([],))])
def test_chapters_write(input_param, expected):
    with patch('builtins.open', mock_open(read_data=input_param)):
        chapters_write()
        assert open.mock_calls[5][1] == expected


@pytest.mark.parametrize('input_param, expected', [('aaAA', 'small letters: 50.0%, big letters: 50.0%'),
                                                   ('aaa', 'small letters: 100.0%, big letters: 0.0%'),
                                                   ('AAA', 'small letters: 0.0%, big letters: 100.0%')])
def test_small_big_letters(input_param, expected, monkeypatch, capsys):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    small_big_letters()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
