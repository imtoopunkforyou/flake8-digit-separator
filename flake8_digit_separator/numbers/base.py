from dataclasses import dataclass

from flake8_digit_separator.validators.cleaner import Cleaner
from flake8_digit_separator.validators.enums import (
    NumberDelimiter,
    NumberPrefix,
    NumeralSystem,
)


@dataclass(frozen=True)
class Number:
    token: str
    numeral_system: NumeralSystem
    is_supported: bool

    @property
    def cleaned_token(self) -> str:
        cleaner = Cleaner(self.token)

        return cleaner.clean()


@dataclass(frozen=True)
class NumberWithPrefix(Number):
    prefix: NumberPrefix


@dataclass(frozen=True)
class NumberWithDelimiter(Number):
    delimiter: NumberDelimiter
