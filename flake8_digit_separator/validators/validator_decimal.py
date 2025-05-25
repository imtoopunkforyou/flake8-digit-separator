import re
from numbers import Number
from typing import TypeVar, final

from flake8_digit_separator.rules.rules import DecimalFDSRules
from flake8_digit_separator.transformations.cleaner import Cleaner
from flake8_digit_separator.validators.base import NumberWithOutPrefixValidator
from flake8_digit_separator.validators.constants import SEPARATOR

SelfDecimalValidator = TypeVar('SelfDecimalValidator', bound='DecimalValidator')


@final
class DecimalValidator(NumberWithOutPrefixValidator):
    def __init__(self: SelfDecimalValidator, number: Number) -> None:
        self._number = number
        self._minimum_length = 4
        self._pattern = r'^\d{1,3}(?:_\d{3})+$'

    def validate(self: SelfDecimalValidator) -> bool:  # noqa: WPS231
        if not self.validate_token_as_int():
            return False

        parts: list[str, str] = self.number.token.split(self.number.delimiter)
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
        return self._pattern

    @property
    def minimum_length(self: SelfDecimalValidator) -> int:
        return self._minimum_length

    @property
    def number(self: SelfDecimalValidator) -> str:
        return self._number

    @property
    def error_message(self: SelfDecimalValidator) -> str:
        return DecimalFDSRules.FDS200.create_message()
