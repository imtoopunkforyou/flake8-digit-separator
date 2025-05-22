import re

from flake8_digit_separator.numbers.base import Number
from flake8_digit_separator.validators.base import Validator
from flake8_digit_separator.validators.cleaner import Cleaner
from flake8_digit_separator.validators.constants import SEPARATOR


class NumberWithPrefixValidator(Validator):
    def __init__(self, number: str) -> None:
        self._number = number
        self._minimum_length = 5

    def validate(self):
        if not self.validate_token_as_int():
            return False
        if not self.validate_length():
            return False
        if not self.number.token.startswith(self.number.prefix):
            return False

        if len(self.number.cleaned_token) >= 5:
            if not re.fullmatch(self.pattern, self.number.token[3:]):
                return False

        return True

    @property
    def number(self) -> Number:
        return self._number

    @property
    def minimum_length(self):
        return self._minimum_length


class HexValidator(NumberWithPrefixValidator):
    def __init__(self, number: str) -> None:
        self._pattern = r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$'
        super().__init__(number=number)

    @property
    def pattern(self) -> str:
        return self._pattern

    @property
    def error_message(self):
        return 'FDS400: HEX'


class BinaryValidator(NumberWithPrefixValidator):
    def __init__(self, number: str) -> None:
        self._pattern = r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$'
        super().__init__(number=number)

    @property
    def pattern(self):
        return self._pattern

    @property
    def error_message(self):
        return 'FDS300: BINARY'


class OctalValidator(Validator):
    def __init__(self, number: Number):
        self._number = number
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'
        self._minimum_length = 4

    def validate(self):
        if not self.validate_token_as_int():
            return False

        if not self.number.token.startswith(self.number.prefix):
            return False
        if not self.validate_length():
            return False

        if len(self.number.cleaned_token) >= 4:
            if not re.fullmatch(self.pattern, self.number.token):
                return False

        return True

    @property
    def minimum_length(self):
        return self._minimum_length

    @property
    def number(self):
        return self._number

    @property
    def pattern(self):
        return self._pattern

    @property
    def error_message(self):
        return 'FDS200: OCT'


class IntValidator(Validator):
    def __init__(self, number: Number) -> None:
        self._number = number
        self._minimum_length = 4
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
        if not self.validate_length():
            return False
        if len(self.number.cleaned_token) >= 4:
            if not re.fullmatch(self.pattern, self.number.token):
                return False

        return True

    @property
    def pattern(self):
        return self._pattern

    @property
    def minimum_length(self):
        return self._minimum_length

    @property
    def number(self):
        return self._number

    @property
    def error_message(self):
        return 'FDS100: INT'


class DecimalValidator(IntValidator):
    def validate(self):  # noqa: WPS231
        if not self.validate_token_as_int():
            return False

        parts: list[str, str] = self.number.token.split(self.number.delimiter)

        for part in parts:
            cleaned_part = Cleaner(part).clean()
            if len(cleaned_part) >= 4:
                if not re.fullmatch(self.pattern, part):
                    return False
            elif len(cleaned_part) < 4 and SEPARATOR in part:
                return False

        return True

    @property
    def error_message(self):
        return 'FDS400: DECIMAL/FLOAT'

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
