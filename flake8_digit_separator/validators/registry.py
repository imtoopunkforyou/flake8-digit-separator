from typing import final

from flake8_digit_separator.fds_numbers.base import FDSNumber
from flake8_digit_separator.fds_numbers.fds_numbers import (
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
from typing import TypeVar

SelfValidatorRegistry = TypeVar('SelfValidatorRegistry', bound='ValidatorRegistry')


@final
class ValidatorRegistry:
    mapping: dict[type[FDSNumber], type[Validator]] = {
        IntNumber: IntValidator,
        HexNumber: HexValidator,
        OctalNumber: OctalValidator,
        BinaryNumber: BinaryValidator,
        DecimalNumber: DecimalValidator,
    }

    @classmethod
    def get_validator(cls: type[SelfValidatorRegistry], number: FDSNumber) -> Validator:
        validator_cls = cls.mapping.get(number.__class__)
        if not validator_cls:
            msg = 'No validator registered for {number}'
            raise ValueError(
                msg.format(
                    number=number.__class__,
                )
            )

        return validator_cls(number)
