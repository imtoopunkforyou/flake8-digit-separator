import enum
from typing import TypeAlias, TypeVar

NumberWithSeparators: TypeAlias = str

SelfFDSRules = TypeVar('SelfFDSRules', bound='FDSRules')


class FDSRules(enum.Enum):
    def __init__(
        self: SelfFDSRules,
        text: str,
        example: NumberWithSeparators,
    ):
        self._text = text
        self._example = example

    def create_message(self: SelfFDSRules) -> str:
        msg = '{rule}: {text} (e.g. {example})'

        return msg.format(
            rule=self.name,
            text=self.value,
            example=self.example,
        )

    @property
    def text(self: SelfFDSRules):
        return self._text

    @property
    def example(self: SelfFDSRules):
        return self._example


class FDSIntRules(FDSRules):
    FDS100 = 'Group by 3s from right', '10_000'


class FDSDecimalRules(FDSRules):
    FDS200 = 'Group by 3s from right', '10_000.1_234'


class FDSBinaryRules(FDSRules):
    FDS300 = 'Group by 4s from right after prefix `0b`', '0b_10_1000'


class FDSOctalRules(FDSRules):
    FDS400 = 'Group by 3s from right after prefix `0o`', '0o_10_100_100'


class FDSHexRules(FDSRules):
    FDS500 = 'Group by 4s from right after prefix `0x`', '0x_CAFE_F00D'
