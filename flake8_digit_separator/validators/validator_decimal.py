import re
from numbers import Number
from typing import final

from flake8_digit_separator.transformations.cleaner import Cleaner
from flake8_digit_separator.validators.base import Validator
from flake8_digit_separator.validators.constants import SEPARATOR


@final
class DecimalValidator(Validator):
    def __init__(self, number: Number) -> None:
        self._number = number
        self._minimum_length = 4
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'

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
