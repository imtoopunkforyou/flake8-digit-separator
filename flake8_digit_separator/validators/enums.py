import enum


@enum.unique
class NumeralSystem(enum.Enum):
    BINARY = 2
    OCTAL = 8
    DECIMAL = 10
    HEX = 16


@enum.unique
class NumberPrefix(enum.Enum):
    BINARY = '0b'
    OCTAL = '0o'
    HEX = '0x'

    def w_separator(self):
        template = '{prefix}_'

        return template.format(
            prefix=self,
        )


@enum.unique
class NumberDelimiter(enum.Enum):
    DECIMAL = '.'
