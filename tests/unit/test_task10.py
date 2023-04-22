import pytest
from printing_imitation import print_models, show_completed_models


@pytest.mark.parametrize('unprinted_designs, completed_models, expected',
                         [(['second design', 'first design'],
                           [], 'Printing model: first design\nPrinting model: second design'),
                          ([-1, 0, 1], [],
                           'Printing model: 1\nPrinting model: 0\nPrinting model: -1'),
                          ([], [], '')])
def test_print_models(unprinted_designs, completed_models, expected, capsys):
    print_models(unprinted_designs, completed_models)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('completed_models, expected',
                         [(['first model', 'second model'],
                           'The following models have been printed:\nfirst model\nsecond model'),
                          ([-1, 0, 1], 'The following models have been printed:\n-1\n0\n1'),
                          ([], 'The following models have been printed:')])
def test_show_completed_models(completed_models, expected, capsys):
    show_completed_models(completed_models)
    captured = capsys.readouterr()
    print(captured)
    assert captured.out.strip() == expected