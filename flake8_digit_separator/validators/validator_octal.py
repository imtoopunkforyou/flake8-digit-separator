from typing import TypeVar, final

from flake8_digit_separator.fds_numbers.fds_numbers import OctalNumber
from flake8_digit_separator.rules.rules import OctalFDSRules
from flake8_digit_separator.validators.base import NumberWithPrefixValidator

SelfOctalValidator = TypeVar('SelfOctalValidator', bound='OctalValidator')


@final
class OctalValidator(NumberWithPrefixValidator):
    def __init__(self: SelfOctalValidator, number: OctalNumber):
        self._number = number
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'
        self._minimum_length = 4

    @property
    def number(self: SelfOctalValidator) -> OctalNumber:
        return self._number

    @property
    def minimum_length(self: SelfOctalValidator) -> int:
        return self._minimum_length

    @property
    def pattern(self: SelfOctalValidator) -> str:
        return self._pattern

    @property
    def error_message(self: SelfOctalValidator) -> str:
        return OctalFDSRules.FDS400.create_message()
