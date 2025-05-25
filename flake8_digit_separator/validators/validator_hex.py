from typing import TypeVar, final

from flake8_digit_separator.fds_numbers.fds_numbers import HexNumber
from flake8_digit_separator.rules.rules import HexFDSRules
from flake8_digit_separator.validators.base import NumberWithPrefixValidator

SelfHexValidator = TypeVar('SelfHexValidator', bound='HexValidator')


@final
class HexValidator(NumberWithPrefixValidator):
    def __init__(self: SelfHexValidator, number: HexNumber) -> None:
        self._pattern = r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$'
        self._minimum_length = 5
        self._number = number

    @property
    def number(self: SelfHexValidator) -> HexNumber:
        """FDS hex number object."""
        return self._number

    @property
    def minimum_length(self: SelfHexValidator) -> int:
        """The minimum token length required to start validation."""
        return self._minimum_length

    @property
    def pattern(self: SelfHexValidator) -> str:
        """The regular expression that will be validated."""
        return self._pattern

    @property
    def error_message(self: SelfHexValidator) -> str:
        """
        The rule that the validator checked.

        :return: FDS rule.
        :rtype: str
        """
        return HexFDSRules.FDS500.create_message()
