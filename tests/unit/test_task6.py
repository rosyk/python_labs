from unittest.mock import patch, mock_open, call
from io import StringIO
import pytest
from task6.rosyk_task6 import numbers_sum, odd_even_write, python_posibilities_print, python_change, \
    guests_greeting, the_counter, text_format, chapters_write, small_big_letters, create_table, \
    insert_ratings, select_all_rows, select_high_ratings


@pytest.mark.parametrize('input_param, expected', [('1\n2\n3', call().write('6.0')), ('0', call().write('0.0'))])
def test_find_sum_numbers(input_param, expected):
    with patch('builtins.open', mock_open(read_data=input_param)):
        numbers_sum()
        open.assert_has_calls([expected])


def test_find_sum_number_string(capsys):
    with patch('builtins.open', mock_open(read_data='string')):
        numbers_sum()
        captured = capsys.readouterr()
        assert captured.out.strip() == 'file contains something except numbers'


@pytest.mark.parametrize('input_param, expected', [(2, call().write('2 is even')), (3, call().write('3 is odd'))])
def test_odd_even_write(input_param, expected):
    with patch('sys.stdin', StringIO(str(input_param))):
        with patch('builtins.open', mock_open(read_data='')):
            odd_even_write()
            open.assert_has_calls([expected])


def test_python_posibilities_print(capsys):
    with patch('builtins.open', mock_open(read_data='in python you can all')):
        python_posibilities_print()
        captured = capsys.readouterr()
        assert captured.out.strip() == 'in python you can all'


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
                                                    'Welcome, John. Have a nice day!'),
                                                   (['exit'], '')])
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


@pytest.mark.parametrize('input_param, expected', [('two\nlines', call().write('two lines')),
                                                   ('one', call().write('one'))])
def test_text_format(input_param, expected):
    with patch('builtins.open', mock_open(read_data=input_param)):
        text_format()
        open.assert_has_calls([expected])


@pytest.mark.parametrize('input_param, expected', [('CHAPTER 1', call().writelines(['CHAPTER 1'])),
                                                   ('', call().writelines([]))])
def test_chapters_write(input_param, expected):
    with patch('builtins.open', mock_open(read_data=input_param)):
        chapters_write()
        open.assert_has_calls([expected])


@pytest.mark.parametrize('input_param, expected', [('aaAA', 'small letters: 50.0%, big letters: 50.0%')])
def test_small_big_letters(input_param, expected, monkeypatch, capsys):
    monkeypatch.setattr('builtins.open', mock_open(read_data=input_param))
    small_big_letters()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.fixture
def mock_cursor():
    with patch('task6.rosyk_task6.sql.connect') as mock_connect:
        mock_conn = mock_connect.return_value
        mock_curs = mock_conn.cursor.return_value
        return mock_curs


def test_create_table(mock_cursor):
    create_table(mock_cursor)
    mock_cursor.execute.assert_called_with(
        'CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY, '
        'title VARCHAR(20), '
        'year INT, '
        'rating FLOAT)'
    )


def test_insert_ratings(mock_cursor):
    insert_ratings(mock_cursor)
    mock_cursor.executemany.assert_called_with(
        'INSERT INTO ratings VALUES(?, ?, ?, ?)',
        [
            (0, "The last of us", 2023, 9.0),
            (1, "Everything Everywhere All at Once", 2022, 7.9),
            (2, "Avatar: way of water", 2023, 7.8),
            (3, "The Whale", 2023, 7.8)
        ]
    )


def test_select_all_rows(mock_cursor, capsys):
    rows = [(1, 'Title 1'), (2, 'Title 2'), (3, 'Title 3')]
    mock_cursor.fetchall.return_value = rows
    select_all_rows(mock_cursor)
    captured = capsys.readouterr()
    assert captured.out.strip() == "(1, 'Title 1')\n(2, 'Title 2')\n(3, 'Title 3')"


def test_select_high_rating(mock_cursor, capsys):
    rows = [(1, 'high rating')]
    mock_cursor.fetchall.return_value = rows
    select_high_ratings(mock_cursor)
    captured = capsys.readouterr()
    assert captured.out.strip() == "(1, 'high rating')"
