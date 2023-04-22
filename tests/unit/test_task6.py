import pytest
from unittest.mock import patch, mock_open
from task6.rosyk_task6 import numbers_sum, odd_even_write


# @pytest.mark.parametrize('input_param, expected', [('1\n2\n3', '6')])
# def test_numbers_sum(input_param, expected, capsys):
#     with patch('builtins.open', mock_open(read_data=input_param)):
#         captured = capsys.readouterr()
#         assert captured.out.strip() == expected


@pytest.mark.parametrize('input_param, expected', [(2, '2 is even')])
def test_odd_even_write(input_param, expected):
    with patch('utils.number_validation_input', return_value=input_param):
        odd_even_write()
        assert open('task6/even_or_odd.txt').read() == expected
