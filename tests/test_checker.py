import pytest

from flake8_digit_separator.checker import Classifier

mapa = {
    '123': 'int',
    '0x1aF': 'hex',
    '0b1010': 'binary',
    '0o777': 'octal',
    '123.45': 'decimal',
    '1e5': 'scientific',
    '123j': 'complex',
    '0x1a.j': 'complex',
    '1_000_000': 'int',
    '123.45e-6': 'scientific',
    '.567': 'decimal',
    '0x1a_bc': 'hex',
    '-0o123': 'octal',
    '+123.45J': 'complex'
}


@pytest.mark.parametrize(
    'number', mapa.keys(),
)
def test_classifier(number):
    c = Classifier(number)
    n = c.classify().type_name
    print('*'*10)
    print(n)
    print('*'*10)

    assert n == mapa.get(number)