import re
from typing import TypeVar, final

from flake8_digit_separator.fds_numbers.fds_numbers import DecimalNumber
from flake8_digit_separator.rules.rules import DecimalFDSRules
from flake8_digit_separator.transformations.cleaner import Cleaner
from flake8_digit_separator.validators.base import NumberWithOutPrefixValidator
from flake8_digit_separator.validators.constants import SEPARATOR

SelfDecimalValidator = TypeVar('SelfDecimalValidator', bound='DecimalValidator')


@final
class DecimalValidator(NumberWithOutPrefixValidator):
    def __init__(self: SelfDecimalValidator, number: DecimalNumber) -> None:
        self._number = number
        self._minimum_length = 4
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'

    def validate(self: SelfDecimalValidator) -> bool:  # noqa: WPS231
        """
        Validating decimal numbers.

        1. Check that we can convert the number to int
        2. Divide the number into two parts by delimeter.
        3. Check that part of number is less than the required minimum length and there is no separator.
        4. Check part of number by pattern.

        :return: `True` if all restrictions have been passed. Otherwise `False`.
        :rtype: bool
        """
        if not self.validate_token_as_int():
            return False

        parts: list[str] = self.number.token.split(self.number.delimiter.value)
        for part in parts:
            cleaned_part = Cleaner(part).clean()
            if len(cleaned_part) >= 4:
                if not re.fullmatch(self.pattern, part):
                    return False
            elif len(cleaned_part) < 4 and SEPARATOR in part:
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
    def minimum_length(self: SelfDecimalValidator) -> int:
        """
        The minimum token length required to start validation.

        :return: Minimum token length.
        :rtype: int
        """
        return self._minimum_length

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
