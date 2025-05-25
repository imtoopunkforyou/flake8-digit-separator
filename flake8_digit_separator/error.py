from dataclasses import astuple, dataclass

from flake8_digit_separator.types import ErrorMessage


@dataclass(frozen=True)
class Error:
    line: int
    column: int
    message: str
    object_type: type[object]

    def as_tuple(self) -> ErrorMessage:
        return astuple(self)
