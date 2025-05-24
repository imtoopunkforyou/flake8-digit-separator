from dataclasses import dataclass

from flake8_digit_separator.fds_numbers.base import (
    Number,
    NumberWithDelimiter,
    NumberWithPrefix,
)
from flake8_digit_separator.fds_numbers.enums import (
    NumberDelimiter,
    NumberPrefix,
    NumeralSystem,
)


@dataclass(frozen=True)
class IntNumber(Number):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL.value
    is_supported: bool = True


@dataclass(frozen=True)
class HexNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.HEX.value
    is_supported: bool = True
    prefix: NumberPrefix = NumberPrefix.HEX.value


@dataclass(frozen=True)
class OctalNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.OCTAL.value
    is_supported: bool = True
    prefix: NumberPrefix = NumberPrefix.OCTAL.value


@dataclass(frozen=True)
class DecimalNumber(NumberWithDelimiter):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL.value
    is_supported: bool = True
    delimiter: NumberDelimiter = NumberDelimiter.DECIMAL.value


@dataclass(frozen=True)
class BinaryNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.BINARY.value
    is_supported: bool = True
    prefix: NumberPrefix = NumberPrefix.BINARY.value


@dataclass(frozen=True)
class ComplexNumber(Number):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL.value
    is_supported: bool = False


@dataclass(frozen=True)
class ScientificNumber(Number):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL.value
    is_supported: bool = False
