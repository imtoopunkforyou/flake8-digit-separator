from dataclasses import dataclass

from flake8_digit_separator.fds_numbers.base import (
    FDSNumber,
    NumberWithDelimiter,
    NumberWithPrefix,
)
from flake8_digit_separator.fds_numbers.enums import (
    NumberDelimiter,
    NumberPrefix,
    NumeralSystem,
)


@dataclass(frozen=True)
class IntNumber(FDSNumber):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL
    is_supported: bool = True


@dataclass(frozen=True)
class HexNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.HEX
    is_supported: bool = True
    prefix: NumberPrefix = NumberPrefix.HEX


@dataclass(frozen=True)
class OctalNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.OCTAL
    is_supported: bool = True
    prefix: NumberPrefix = NumberPrefix.OCTAL


@dataclass(frozen=True)
class DecimalNumber(NumberWithDelimiter):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL
    is_supported: bool = True
    delimiter: NumberDelimiter = NumberDelimiter.DECIMAL.value


@dataclass(frozen=True)
class BinaryNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.BINARY
    is_supported: bool = True
    prefix: NumberPrefix = NumberPrefix.BINARY


@dataclass(frozen=True)
class ComplexNumber(FDSNumber):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL
    is_supported: bool = False


@dataclass(frozen=True)
class ScientificNumber(FDSNumber):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL
    is_supported: bool = False
