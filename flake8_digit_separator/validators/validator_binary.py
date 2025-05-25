from numbers import Number
from typing import TypeVar, final

from flake8_digit_separator.rules.rules import BinaryFDSRules
from flake8_digit_separator.validators.base import NumberWithPrefixValidator

SelfBinaryValidator = TypeVar('SelfBinaryValidator', bound='BinaryValidator')


@final
class BinaryValidator(NumberWithPrefixValidator):
    def __init__(self: SelfBinaryValidator, number: str) -> None:
        self._pattern = r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$'
        self._minimum_length = 5
        self._number = number

    @property
    def number(self: SelfBinaryValidator) -> Number:
        return self._number

    @property
    def minimum_length(self: SelfBinaryValidator) -> str:
        return self._minimum_length

    @property
    def pattern(self: SelfBinaryValidator) -> str:
        return self._pattern

    @property
    def error_message(self: SelfBinaryValidator) -> str:
        return BinaryFDSRules.FDS300.create_message()
