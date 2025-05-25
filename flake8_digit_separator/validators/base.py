import re
from abc import ABC, abstractmethod
from typing import TypeVar

from flake8_digit_separator.fds_numbers.base import (
    FDSNumber,
    NumberWithDelimiter,
    NumberWithPrefix,
)
from flake8_digit_separator.validators.constants import SEPARATOR

SelfValidator = TypeVar('SelfValidator', bound='Validator')
SelfBaseValidator = TypeVar('SelfBaseValidator', bound='BaseValidator')
SelfNumberWithPrefixValidator = TypeVar('SelfNumberWithPrefixValidator', bound='NumberWithPrefixValidator')
SelfNumberWithOutPrefixValidator = TypeVar('SelfNumberWithOutPrefixValidator', bound='NumberWithOutPrefixValidator')


class Validator(ABC):
    @property
    @abstractmethod
    def number(self: SelfValidator) -> FDSNumber | NumberWithDelimiter | NumberWithPrefix:
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
    def validate(self: SelfValidator) -> bool:
        ...

    @property
    @abstractmethod
    def error_message(self: SelfValidator) -> str:
        ...


class BaseValidator(Validator):
    def validate_length(self: SelfBaseValidator) -> bool:
        if (
            (len(self.number.cleaned_token) < self.minimum_length)
            and (SEPARATOR in self.number.token)
        ):
            return False

        return True

    def validate_token_as_int(self: SelfBaseValidator) -> bool:
        try:
            int(self.number.token, self.number.numeral_system.value)
        except ValueError:
            return False

        return True


class NumberWithPrefixValidator(BaseValidator):
    def validate(self: SelfNumberWithPrefixValidator) -> bool:
        if not self.validate_token_as_int():
            return False
        if not self.validate_length():
            return False
        if not self.number.token.startswith(self.number.prefix.value):
            return False

        if len(self.number.cleaned_token) >= self.minimum_length:
            if not re.fullmatch(self.pattern, self.number.token[3:]):
                return False

        return True

    @property
    def number(self: SelfNumberWithPrefixValidator) -> NumberWithPrefix:
        raise NotImplementedError('A number with a prefix must be specified.')


class NumberWithOutPrefixValidator(BaseValidator):
    """Docst docstr"""
