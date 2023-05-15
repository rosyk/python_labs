from unittest.mock import patch, mock_open
from io import StringIO
import pytest
from task6.rosyk_task6 import numbers_sum, odd_even_write, python_posibilities_print, python_change, \
    guests_greeting, the_counter, text_format, chapters_write, small_big_letters, imdb_rating


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


def test_imdb_ratings(capsys):
    with patch('task6.rosyk_task6.sql') as mock_sql:
        mock_conn = mock_sql.connect.return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = (4,)
        imdb_rating()
        mock_sql.connect.assert_called_once_with('task6/imdb.db')
        mock_cursor.execute.assert_any_call('CREATE TABLE IF NOT EXISTS ratings '
                                            '(id INTEGER PRIMARY KEY, title VARCHAR(20), year INT, rating FLOAT)')
        assert mock_cursor.execute.call_count == 7
        mock_conn.commit.assert_called_once()
    expected_return = '''(2, 'Avatar: way of water', 2023, 7.8)
(1, 'Everything Everywhere All at Once', 2022, 7.9)
(3, 'The Whale', 2023, 7.8)
(0, 'The last of us', 2023, 9.0)
(0, 'The last of us', 2023, 9.0)'''
    imdb_rating()
    captured = capsys.readouterr()
    print(captured.out.strip())
    print(expected_return)
    print(captured.out.strip() == expected_return)
    assert captured.out.strip() == expected_return
