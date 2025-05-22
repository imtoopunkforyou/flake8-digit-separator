from typing import final

from flake8_digit_separator.numbers.base import Number
from flake8_digit_separator.numbers.numbers import (
    BinaryNumber,
    DecimalNumber,
    HexNumber,
    IntNumber,
    OctalNumber,
)
from flake8_digit_separator.validators.base import Validator
from flake8_digit_separator.validators.validator_binary import BinaryValidator
from flake8_digit_separator.validators.validator_decimal import DecimalValidator
from flake8_digit_separator.validators.validator_hex import HexValidator
from flake8_digit_separator.validators.validator_int import IntValidator
from flake8_digit_separator.validators.validator_octal import OctalValidator


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
