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

    def validate(self):
        ...

    @property
    def error_message(self):
        ...


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

    def validate(self):
        ...

    @property
    def error_message(self):
        ...


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

    def validate(self):
        ...

    @property
    def error_message(self):
        ...


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

    def validate(self):
        ...

    @property
    def error_message(self):
        ...


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

    def validate(self):
        ...

    @property
    def error_message(self):
        ...


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

    def validate(self):
        return ...

    @property
    def error_message(self):
        ...


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

    def validate(self) -> bool | str:
        token = self.token.lstrip('+-')
        cleaned = token.replace('_', '')

        if len(cleaned) >= 4:
            if '_' in token:
                if not re.fullmatch(r'^\d{1,3}(?:_\d{3})+$', token):
                    return False
            else:
                return False

        return True

    @property
    def error_message(self):
        return 'FDS: Hello World!!!!!!!!!(PEP515)'


a = 1000_0
