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
    def text(self: SelfFDSRules) -> str:
        return self._text

    @property
    def example(self: SelfFDSRules) -> NumberWithSeparators:
        return self._example
