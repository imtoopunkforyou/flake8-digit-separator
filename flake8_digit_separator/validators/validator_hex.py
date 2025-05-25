from numbers import Number
from typing import TypeVar, final

from flake8_digit_separator.rules.rules import HexFDSRules
from flake8_digit_separator.validators.base import NumberWithPrefixValidator

SelfHexValidator = TypeVar('SelfHexValidator', bound='HexValidator')


@final
class HexValidator(NumberWithPrefixValidator):
    def __init__(self: SelfHexValidator, number: str) -> None:
        self._pattern = r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$'
        self._minimum_length = 5
        self._number = number

    @property
    def number(self: SelfHexValidator) -> Number:
        return self._number

    @property
    def minimum_length(self: SelfHexValidator) -> int:
        return self._minimum_length

    @property
    def pattern(self: SelfHexValidator) -> str:
        return self._pattern

    @property
    def error_message(self: SelfHexValidator) -> str:
        return HexFDSRules.FDS500.create_message()
