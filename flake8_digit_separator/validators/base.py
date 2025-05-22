import re
from abc import ABC, abstractmethod

from flake8_digit_separator.numbers.base import Number
from flake8_digit_separator.validators.constants import SEPARATOR


class Validator(ABC):
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

    @property
    @abstractmethod
    def number(self) -> Number:
        ...

    @property
    @abstractmethod
    def pattern(self) -> str:
        ...

    @property
    @abstractmethod
    def minimum_length(self) -> int:
        ...

    @abstractmethod
    def validate(self):
        ...

    @property
    @abstractmethod
    def error_message(self):
        ...


class NumberWithPrefixValidator(Validator):
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


