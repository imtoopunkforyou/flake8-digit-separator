from dataclasses import dataclass
from typing import TypeAlias, TypeVar

from flake8_digit_separator.fds_numbers.enums import (
    NumberDelimiter,
    NumberPrefix,
    NumeralSystem,
)
from flake8_digit_separator.transformations.cleaner import Cleaner

SelfFDSNumber = TypeVar('SelfFDSNumber', bound='FDSNumber')

CleanedToken: TypeAlias = str
NumberTokenLikeStr: TypeAlias = str


@dataclass(frozen=True)
class FDSNumber:
    token: NumberTokenLikeStr
    numeral_system: NumeralSystem
    is_supported: bool

    @property
    def cleaned_token(self: SelfFDSNumber) -> CleanedToken:
        cleaner = Cleaner(self.token)

        return cleaner.clean()


@dataclass(frozen=True)
class NumberWithPrefix(FDSNumber):
    prefix: NumberPrefix


@dataclass(frozen=True)
class NumberWithDelimiter(FDSNumber):
    delimiter: NumberDelimiter
