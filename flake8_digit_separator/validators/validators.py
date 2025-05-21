import re

from validators.constants import SEPARATOR

from flake8_digit_separator.validators.base import Validator
from flake8_digit_separator.validators.cleaner import Cleaner
from flake8_digit_separator.validators.enums import NumeralSystem
from flake8_digit_separator.validators.numbers import Number


class HexValidator(NumberValidator):
    def __init__(self, token: str):
        self._token = token

    @property
    def numeral_system(self) -> NumeralSystem:
        return NumeralSystem.HEX.value

    @property
    def token(self):
        return self._token

    def check(self) -> bool:
        try:
            int(self.token, self.numeral_system)
        except ValueError:
            return False

        return True

    def validate(self):
        token = self.token.lstrip('+-').lower()
        cleaned = token.replace('_', '')
        
        if not token.startswith('0x_'):
            return False
        elif len(cleaned) >= 5:
            if '_' in token:
                if not re.fullmatch(r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$', token[3:]):
                    return False
            else:
                return False
        elif len(cleaned) < 5 and '_' in cleaned:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS400: HEX'


class BinaryClassifier(NumberValidator):
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
        token = self.token.lstrip('+-').lower()
        cleaned = token.replace('_', '')

        if not token.startswith('0b_'):
            return False
        elif len(cleaned) >= 5:
            if '_' in token:
                if not re.fullmatch(r'^\d{1,4}(?:_\d{4})+$', token[3:]):
                    return False
            else:
                return False
        elif len(cleaned) < 5 and '_' in cleaned:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS300: BINARY'


class OctalClassifier(NumberValidator):
    def __init__(self, token: str):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'octal'

    @property
    def re_expression(self):
        ...

    def check(self) -> bool:
        token: str = self.token.lower().lstrip('+-').replace('_', '')
        token_without_prefix: str = token[2:]
        octal_digits: set[str] = set(str(digit) for digit in range(8))

        try:
            int(token, 8)
        except ValueError:
            return False

        return bool(
            token.startswith('0o')
            and all(digit in octal_digits for digit in token_without_prefix)
        )

    def validate(self):
        token = self.token.lstrip('+-').lower()
        cleaned = token.replace('_', '')

        if not token.startswith('0o_'):
            return False
        elif len(cleaned) >= 4:
            if '_' in token:
                if not re.fullmatch(r'^\d{1,3}(?:_\d{3})+$', token[3:]):
                    return False
            else:
                return False
        elif len(cleaned) < 4 and '_' in cleaned:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS200: OCT'


class DecimalClassifier(NumberValidator):
    def __init__(self, token: str):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'decimal'

    def check(self) -> bool:
        if '.' in self.token:
            sep = self.token.split('.')
            if len(sep) == 2:
                left, right = sep[0], sep[1]
                try:
                    if left != '':
                        int(left, 10)
                        int(right, 10)
                        return True
                    else:
                        int(right, 10)
                        return True
                except ValueError:
                    return False
                
        return False

    def validate(self):
        token = self.token.lstrip('+-')

        parts = token.split('.')

        for part in parts:
            cleaned = part.replace('_', '')
            if len(cleaned) >= 4:
                if '_' in token:
                    if not re.fullmatch(r'^\d{1,3}(?:_\d{3})+$', part):
                        return False
                else:
                    return False
            elif len(cleaned) < 4 and '_' in part:
                return False

        return True

    @property
    def error_message(self):
        return 'FDS400: DECIMAL/FLOAT'


class IntValidator(Validator):
    def __init__(self, number: Number) -> None:
        self._number = number
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'
        self._slice_size = 4

    def validate(self) -> bool:
        """
        Wrong: 100000, 10000_0, 1_0000, 10_00000
        Correct: 1_000, 10_000, 100_000, 10, 100, 10_000_000

        :return: _description_
        :rtype: bool
        """
        if not self.validate_supported:
            return False

        if not self.validate_token_as_int():
            return False

        token = self.number.token
        cleaned_token = Cleaner(token).clean()
        if len(cleaned_token) < self._slice_size and SEPARATOR in token:
            return False
        if len(cleaned_token) >= self._slice_size:
            if not re.fullmatch(self.pattern, token):
                return False

        return True

    @property
    def slice_size(self):
        return self._slice_size

    @property
    def number(self):
        return self._number

    @property
    def pattern(self):
        return self._pattern

    @property
    def error_message(self):
        return 'FDS100: INT'


a = 100
a = 10_0000

b = 0o_360_363
b = 0o_360_363_0

с = 0b_0_0111_1110_1001_1100
с = 0b_0_0111_1110_1001_1100_0

d = 0x_CAFE_F00D
d = 0x_CAFE_F00D_0

e = 12_123.1_231_231
e = 12_123.1_231_231_0