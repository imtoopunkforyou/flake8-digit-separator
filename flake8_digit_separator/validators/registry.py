from typing import TypeAlias, TypeVar, final

from flake8_digit_separator.fds_numbers.fds_numbers import (
    BinaryNumber,
    DecimalNumber,
    HexNumber,
    IntNumber,
    OctalNumber,
)
from flake8_digit_separator.validators.validator_binary import BinaryValidator
from flake8_digit_separator.validators.validator_decimal import DecimalValidator
from flake8_digit_separator.validators.validator_hex import HexValidator
from flake8_digit_separator.validators.validator_int import IntValidator
from flake8_digit_separator.validators.validator_octal import OctalValidator

SelfValidatorRegistry = TypeVar('SelfValidatorRegistry', bound='ValidatorRegistry')

ValidatorsWithPrefixAlias: TypeAlias = HexValidator | OctalValidator | BinaryValidator
ValidatorsWithOutPrefixAlias: TypeAlias = IntValidator | DecimalValidator
ValidatorsAlias: TypeAlias = ValidatorsWithPrefixAlias | ValidatorsWithOutPrefixAlias

FDSNumbersWithPrefixAlias: TypeAlias = HexNumber | OctalNumber | BinaryNumber
FDSNumbersWithOutPrefixAlias: TypeAlias = IntNumber | DecimalNumber
FDSNumbersAlias: TypeAlias = FDSNumbersWithOutPrefixAlias | FDSNumbersWithPrefixAlias


@final
class ValidatorRegistry:
    mapping: dict[type[FDSNumbersAlias], type[ValidatorsAlias]] = {
        IntNumber: IntValidator,
        HexNumber: HexValidator,
        OctalNumber: OctalValidator,
        BinaryNumber: BinaryValidator,
        DecimalNumber: DecimalValidator,
    }

    @classmethod
    def get_validator(cls: type[SelfValidatorRegistry], number: FDSNumbersAlias) -> ValidatorsAlias:
        validator_cls: type[ValidatorsAlias] | None = cls.mapping.get(number.__class__)
        if not validator_cls:
            msg = 'No validator registered for {number}'
            raise ValueError(
                msg.format(
                    number=number.__class__,
                )
            )

        return validator_cls(number)  # type: ignore [arg-type]
