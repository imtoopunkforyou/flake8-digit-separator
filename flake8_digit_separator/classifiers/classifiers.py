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

    @property
    def re_expression(self):
        return (
            r'^[+-]?('
            r'('
            r'\d[\d_]*(\.\d[\d_]*)?([eE][+-]?\d[\d_]*)?|'    # Decimal numbers
            r'\.\d[\d_]*([eE][+-]?\d[\d_]*)?|'               # Numbers starting with a point
            r'0[xX][\da-fA-F_]+(\.[\da-fA-F_]*)?|'           # HEX with decimal point
            r'0[bB][01_]+|'                                  # Binary numbers
            r'0[oO][0-7_]+'                                  # Octal numbers
            r')'
            r')[jJ]$'
        )

    def check(self) -> bool:
        return bool(re.fullmatch(
            self.re_expression,
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

    @property
    def re_expression(self):
        return r'^[+-]?0[xX][\da-fA-F_]+$'

    def check(self) -> bool:
        return bool(re.fullmatch(self.re_expression, self.token))


class BinaryClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'binary'

    @property
    def re_expression(self):
        return r'^[+-]?0[bB][01_]+$'

    def check(self) -> bool:
        return bool(re.fullmatch(self.re_expression, self.token))


class OctalClassifier(NumberClassifier):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'octal'

    @property
    def re_expression(self):
        return r'^[+-]?0[oO][0-7_]+$'

    def check(self) -> bool:
        return bool(re.fullmatch(self.re_expression, self.token))


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

    @property
    def re_expression(self):
        return r'^[+-]?\d[\d_]*$'

    def check(self) -> bool:
        return bool(re.fullmatch(self.re_expression, self.token))
