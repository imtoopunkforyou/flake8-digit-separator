from typing import TypeAlias

from flake8_digit_separator.fds_numbers.fds_numbers import (
    BinaryNumber,
    ComplexNumber,
    DecimalNumber,
    HexNumber,
    IntNumber,
    OctalNumber,
    ScientificNumber,
)

FDSNumbersWithPrefixAlias: TypeAlias = HexNumber | OctalNumber | BinaryNumber
FDSNumbersWithOutPrefixAlias: TypeAlias = IntNumber | DecimalNumber
FDSNumbersUnsupported: TypeAlias = ComplexNumber | ScientificNumber
FDSNumbersAlias: TypeAlias = FDSNumbersWithOutPrefixAlias | FDSNumbersWithPrefixAlias | FDSNumbersUnsupported
