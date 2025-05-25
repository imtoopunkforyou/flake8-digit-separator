from typing import TypeAlias

from flake8_digit_separator.fds_numbers.fds_numbers import (
    BinaryNumber,
    DecimalNumber,
    HexNumber,
    IntNumber,
    OctalNumber,
)

FDSNumbersWithPrefixAlias: TypeAlias = HexNumber | OctalNumber | BinaryNumber
FDSNumbersWithOutPrefixAlias: TypeAlias = IntNumber | DecimalNumber
FDSNumbersAlias: TypeAlias = FDSNumbersWithOutPrefixAlias | FDSNumbersWithPrefixAlias
