import re
from numbers import Number
from typing import final

from flake8_digit_separator.validators.base import Validator


@final
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
