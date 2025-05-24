import re
from abc import ABC, abstractmethod
from typing import TypeVar

from flake8_digit_separator.fds_numbers.base import Number
from flake8_digit_separator.validators.constants import SEPARATOR

SelfValidator = TypeVar('SelfValidator', bound='Validator')
SelfBaseValidator = TypeVar('SelfBaseValidator', bound='BaseValidator')
SelfNumberWithPrefixValidator = TypeVar('SelfNumberWithPrefixValidator', bound='NumberWithPrefixValidator')
SelfNumberWithOutPrefixValidator = TypeVar('SelfNumberWithOutPrefixValidator', bound='NumberWithOutPrefixValidator')


class Validator(ABC):
    @property
    @abstractmethod
    def number(self: SelfValidator) -> Number:
        ...

    @property
    @abstractmethod
    def pattern(self: SelfValidator) -> str:
        ...

    @property
    @abstractmethod
    def minimum_length(self: SelfValidator) -> int:
        ...

    @abstractmethod
    def validate(self) -> bool:
        ...

    @property
    @abstractmethod
    def error_message(self) -> str:
        ...


class BaseValidator(Validator):
    def validate_length(self) -> bool:
        if (
            (len(self.number.cleaned_token) < self.minimum_length)
            and (SEPARATOR in self.number.token)
        ):
            return False

        return True

    def validate_token_as_int(self) -> bool:
        try:
            int(self.number.token, self.number.numeral_system)
        except ValueError:
            return False

        return True


class NumberWithPrefixValidator(BaseValidator):
    def validate(self):
        if not self.validate_token_as_int():
            return False
        if not self.validate_length():
            return False
        if not self.number.token.startswith(self.number.prefix):
            return False

        if len(self.number.cleaned_token) >= self.minimum_length:
            if not re.fullmatch(self.pattern, self.number.token[3:]):
                return False

        return True


class NumberWithOutPrefixValidator(BaseValidator):
    """Docst docstr"""
