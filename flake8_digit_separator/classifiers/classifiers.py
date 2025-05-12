import re

from flake8_digit_separator.classifiers.base import NumberClassifier


class ComplexClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'complex'

    def check(self) -> bool:
        return bool(re.fullmatch(
            r'^[+-]?('
            r'('
            r'\d[\d_]*(\.\d[\d_]*)?([eE][+-]?\d[\d_]*)?|'   # Десятичные
            r'\.\d[\d_]*([eE][+-]?\d[\d_]*)?|'              # Числа с точкой в начале
            r'0[xX][\da-fA-F_]+(\.[\da-fA-F_]*)?|'          # HEX с точкой
            r'0[bB][01_]+|'                                 # BIN
            r'0[oO][0-7_]+'                                 # OCT
            r')'
            r')[jJ]$',
            self.token,
            flags=re.IGNORECASE,
        ))


class HexClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'hex'

    def check(self) -> bool:
        return bool(re.fullmatch(r'^[+-]?0[xX][\da-fA-F_]+$', self.token))


class BinaryClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'binary'

    def check(self) -> bool:
        return bool(re.fullmatch(r'^[+-]?0[bB][01_]+$', self.token))


class OctalClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'octal'

    def check(self) -> bool:
        return bool(re.fullmatch(r'^[+-]?0[oO][0-7_]+$', self.token))


class ScientificClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token.lower()

    @property
    def type_name(self):
        return 'scientific'

    def check(self) -> bool:
        return 'e' in self.token


class DecimalClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'decimal'

    def check(self) -> bool:
        return '.' in self.token


class IntClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'int'

    def check(self) -> bool:
        return bool(re.fullmatch(r'^[+-]?\d[\d_]*$', self.token))
