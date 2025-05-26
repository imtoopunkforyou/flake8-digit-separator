import re
from typing import TypeVar, final

from flake8_digit_separator.fds_numbers.fds_numbers import DecimalNumber
from flake8_digit_separator.rules.rules import DecimalFDSRules
from flake8_digit_separator.validators.base import BaseValidator

SelfDecimalValidator = TypeVar('SelfDecimalValidator', bound='DecimalValidator')


@final
class DecimalValidator(BaseValidator):
    def __init__(self: SelfDecimalValidator, number: DecimalNumber) -> None:
        self._number = number
        self._pattern = r'^[+-]?(?:(?!0_)\d{1,3}(?:_\d{3})*\.\d{1,3}(?:_\d{3})*|\.\d{1,3}(?:_\d{3})*)$'

    def validate(self: SelfDecimalValidator) -> bool:
        """
        Validating decimal numbers.

        """
        if not self.validate_token_as_float():
            return False

        if not re.fullmatch(self.pattern, self.number.token):
            return False

        return True

    @property
    def pattern(self: SelfDecimalValidator) -> str:
        """
        The regular expression that will be validated.

        :return: Regular expression.
        :rtype: str
        """
        return self._pattern

    @property
    def number(self: SelfDecimalValidator) -> DecimalNumber:
        """FDS decimal number object."""
        return self._number

    @property
    def error_message(self: SelfDecimalValidator) -> str:
        """
        The rule that the validator checked.

        :return: FDS rule.
        :rtype: str
        """
        return DecimalFDSRules.FDS200.create_message()
