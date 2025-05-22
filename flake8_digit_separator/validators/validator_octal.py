from numbers import Number
from typing import final

from flake8_digit_separator.validators.base import NumberWithPrefixValidator


@final
class OctalValidator(NumberWithPrefixValidator):
    def __init__(self, number: Number):
        self._number = number
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'
        self._minimum_length = 4

    @property
    def number(self) -> Number:
        return self._number

    @property
    def minimum_length(self):
        return self._minimum_length

    @property
    def pattern(self):
        return self._pattern

    @property
    def error_message(self):
        return 'FDS200: OCT'
