from dataclasses import dataclass
from typing import TypeAlias, TypeVar

from flake8_digit_separator.fds_numbers.enums import (
    NumberDelimiter,
    NumberPrefix,
    NumeralSystem,
)
from flake8_digit_separator.transformations.cleaner import Cleaner

SelfNumber = TypeVar('SelfNumber', bound='Number')

CleanedToken: TypeAlias = str


@dataclass(frozen=True)
class Number:
    token: str
    numeral_system: NumeralSystem
    is_supported: bool

    @property
    def cleaned_token(self: SelfNumber) -> CleanedToken:
        cleaner = Cleaner(self.token)

        return cleaner.clean()


@dataclass(frozen=True)
class NumberWithPrefix(Number):
    prefix: NumberPrefix


@dataclass(frozen=True)
class NumberWithDelimiter(Number):
    delimiter: NumberDelimiter
