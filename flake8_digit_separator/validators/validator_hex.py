from numbers import Number

from flake8_digit_separator.validators.base import NumberWithPrefixValidator


class HexValidator(NumberWithPrefixValidator):
    def __init__(self, number: str) -> None:
        self._pattern = r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$'
        self._minimum_length = 5
        self._number = number

    @property
    def number(self) -> Number:
        return self._number

    @property
    def minimum_length(self):
        return self._minimum_length

    @property
    def pattern(self) -> str:
        return self._pattern

    @property
    def error_message(self):
        return 'FDS400: HEX'
