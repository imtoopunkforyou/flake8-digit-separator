from typing import final

from flake8_digit_separator.validators.base import Validator
from flake8_digit_separator.validators.numbers import (
    BinaryNumber,
    HexNumber,
    IntNumber,
    Number,
    OctalNumber,
    DecimalNumber,
)
from flake8_digit_separator.validators.validators import (
    BinaryValidator,
    HexValidator,
    IntValidator,
    OctalValidator,
    DecimalValidator,
)


@final
class ValidatorRegistry:
    mapping: dict[type[Number], type[Validator]] = {
        IntNumber: IntValidator,
        HexNumber: HexValidator,
        OctalNumber: OctalValidator,
        BinaryNumber: BinaryValidator,
        DecimalNumber: DecimalValidator,
    }

    @classmethod
    def get_validator(cls, number: Number) -> Validator:
        validator_cls = cls.mapping.get(number.__class__)
        if not validator_cls:
            msg = 'No validator registered for {number}'
            raise ValueError(
                msg.format(
                    number=number.__class__,
                )
            )

        return validator_cls(number)