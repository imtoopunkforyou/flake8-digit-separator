import re
from typing import Mapping

from flake8_digit_separator.validators.base import Validator
from flake8_digit_separator.validators.cleaner import Cleaner
from flake8_digit_separator.validators.constants import SEPARATOR
from flake8_digit_separator.validators.numbers import (
    BinaryNumber,
    ComplexNumber,
    DecimalNumber,
    HexNumber,
    IntNumber,
    Number,
    OctalNumber,
    ScientificNumber,
)


class HexValidator(Validator):
    def __init__(self, number: str):
        self._number = number
        self._pattern = r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$'


    def validate(self):
        if not self.validate_token_as_int():
            return False
        
        token = self.number.token
        if not token.startswith(self.number.prefix):
            return False

        cleaned_token = Cleaner(token).clean()
        if len(cleaned_token) >= 5:
            if not re.fullmatch(self.pattern, token[3:]):
                return False
        elif len(cleaned_token) < 5 and SEPARATOR in cleaned_token:
            return False

        return True


    @property
    def number(self) -> Number:
        return self._number

    @property
    def pattern(self) -> str:
        return self._pattern

    @property
    def error_message(self):
        return 'FDS400: HEX'

class BinaryValidator(Validator):
    def __init__(self, number: Number) -> None:
        self._number = number
        self._pattern = r'^\d{1,4}(?:_\d{4})+$'

    @property
    def number(self):
        return self._number

    @property
    def pattern(self):
        return self._pattern

    def validate(self):
        if not self.validate_token_as_int():
            return False

        token = self.number.token
        if not token.startswith(self.number.prefix):
            return False

        cleaned_token = Cleaner(token).clean()
        if len(cleaned_token) >= 5:
            if not re.fullmatch(self.pattern, token[3:]):
                return False
        elif len(cleaned_token) < 5 and SEPARATOR in cleaned_token:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS300: BINARY'


class OctalValidator(Validator):
    def __init__(self, number: Number):
        self._number = number
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'

    def validate(self):
        if not self.validate_token_as_int():
            return False

        token = self.number.token
        cleaned_token = Cleaner(token).clean()

        if not token.startswith(self.number.prefix):
            return False

        if len(cleaned_token) >= 4:
            if not re.fullmatch(self.pattern, token[3:]):
                return False
        elif len(cleaned_token) < 4 and SEPARATOR in cleaned_token:
            return False

        return True

    @property
    def number(self):
        return self._number

    @property
    def pattern(self):
        return self._pattern

    @property
    def error_message(self):
        return 'FDS200: OCT'

class DecimalValidator(Validator):
    def __init__(self, number: Number):
        self._number = number
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'

    def validate(self):
        if not self.validate_token_as_int():
            return False

        token = self.number.token
        parts = token.split(self.number.delimiter)

        for part in parts:
            cleaned_part = Cleaner(part).clean()
            if len(cleaned_part) >= 4:
                if not re.fullmatch(self.pattern, part):
                    return False
            elif len(cleaned_part) < 4 and SEPARATOR in part:
                return False

        return True

    @property
    def number(self) -> Number:
        return self._number

    @property
    def pattern(self):
        return self._pattern

    @property
    def error_message(self):
        return 'FDS400: DECIMAL/FLOAT'


class IntValidator(Validator):
    def __init__(self, number: Number) -> None:
        self._number = number
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'

    def validate(self) -> bool:
        """
        Wrong: 100000, 10000_0, 1_0000, 10_00000
        Correct: 1_000, 10_000, 100_000, 10, 100, 10_000_000

        :return: _description_
        :rtype: bool
        """
        if not self.validate_token_as_int():
            return False

        token = self.number.token
        cleaned_token = Cleaner(token).clean()
        if len(cleaned_token) < 4 and SEPARATOR in token:
            return False
        if len(cleaned_token) >= 4:
            if not re.fullmatch(self.pattern, token):
                return False

        return True

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