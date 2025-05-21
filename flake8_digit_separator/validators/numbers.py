from dataclasses import dataclass

from validators.constants import SEPARATOR
from validators.enums import NumberDelimiter, NumberPrefix, NumeralSystem


@dataclass
class Number:
    token: str
    supported: bool = True
    numeral_system: NumeralSystem


@dataclass
class NumberWithPrefix(Number):
    prefix: NumberPrefix


@dataclass
class NumberWithDelimiter(Number):
    delimiter: NumberDelimiter


@dataclass(frozen=True)
class IntNumber(Number):
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL.value


@dataclass(frozen=True)
class HexNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.HEX.value


@dataclass(frozen=True)
class OctalNumber(NumberWithPrefix):
    numeral_system: NumeralSystem = NumeralSystem.OCTAL.value


@dataclass(frozen=True)
class DecimalNumber(NumberWithDelimiter):
    delimiter: NumberDelimiter = NumberDelimiter.DECIMAL.value


@dataclass(frozen=True)
class BinaryNumber(NumberWithPrefix):
    prefix: NumberPrefix = NumberPrefix.BINARY.value
    numeral_system: NumeralSystem = NumeralSystem.BINARY.value


@dataclass(frozen=True)
class ComplexNumber(Number):
    supported: bool = False
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL.value


@dataclass(frozen=True)
class ScientificNumber(Number):
    supported: bool = False
    numeral_system: NumeralSystem = NumeralSystem.DECIMAL.value
