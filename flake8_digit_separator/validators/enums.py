import enum


@enum.unique
class NumeralSystem(enum.Enum):
    BINARY = 2
    OCTAL = 8
    DECIMAL = 10
    HEX = 16


@enum.unique
class NumberPrefix(enum.Enum):
    BINARY = '0b_'
    OCTAL = '0o_'
    HEX = '0x_'

@enum.unique
class NumberDelimiter(enum.Enum):
    DECIMAL = '.'
