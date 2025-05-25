import re
from typing import TypeVar, final

from flake8_digit_separator.fds_numbers.fds_numbers import IntNumber
from flake8_digit_separator.rules.rules import IntFDSRules
from flake8_digit_separator.validators.base import NumberWithOutPrefixValidator

SelfIntValidator = TypeVar('SelfIntValidator', bound='IntValidator')


@final
class IntValidator(NumberWithOutPrefixValidator):
    def __init__(self: SelfIntValidator, number: IntNumber) -> None:
        self._number = number
        self._minimum_length = 4
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'

    def validate(self: SelfIntValidator) -> bool:
        """
        Validating int numbers.

        1. Check that we can convert the number to int
        2. Check that number is less than the required minimum length and there is no separator.
        3. Check number by pattern.

        :return: `True` if all restrictions have been passed. Otherwise `False`.
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
    def pattern(self: SelfIntValidator) -> str:
        """
        The regular expression that will be validated.

        :return: Regular expression.
        :rtype: str
        """
        return self._pattern

    @property
    def minimum_length(self: SelfIntValidator) -> int:
        """
        The minimum token length required to start validation.

        :return: Minimum token length.
        :rtype: int
        """
        return self._minimum_length

    @property
    def number(self: SelfIntValidator) -> IntNumber:
        """FDS int number object"""
        return self._number

    @property
    def error_message(self: SelfIntValidator) -> str:
        """
        The rule that the validator checked.

        :return: FDS rule.
        :rtype: str
        """
        return IntFDSRules.FDS100.create_message()
