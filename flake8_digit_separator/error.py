from dataclasses import astuple, dataclass


@dataclass(frozen=True)
class Error:
    line: int
    column: int
    message: str
    object_type: type[object]

    def as_tuple(self):
        return astuple(self)
