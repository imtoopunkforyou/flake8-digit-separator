import re
from abc import ABC, abstractmethod
from typing import NoReturn, TypeVar

from flake8_digit_separator.fds_numbers.base import (
    FDSNumber,
    NumberWithDelimiter,
    NumberWithPrefix,
)
from flake8_digit_separator.validators.constants import SEPARATOR

SelfValidator = TypeVar('SelfValidator', bound='Validator')
SelfBaseValidator = TypeVar('SelfBaseValidator', bound='BaseValidator')
SelfNumberWithPrefixValidator = TypeVar('SelfNumberWithPrefixValidator', bound='NumberWithPrefixValidator')
SelfNumberWithOutPrefixValidator = TypeVar('SelfNumberWithOutPrefixValidator', bound='NumberWithOutPrefixValidator')
SelfBaseDecimalValidator = TypeVar('SelfBaseDecimalValidator', bound='BaseDecimalValidator')


class Validator(ABC):
    """Abstract validator."""

    @property
    @abstractmethod
    def number(self: SelfValidator) -> FDSNumber | NumberWithDelimiter | NumberWithPrefix:
        """
        Number object obtained from classifier.

        :return: FDSNumber obj.
        :rtype: FDSNumber | NumberWithDelimiter | NumberWithPrefix
        """

    @property
    @abstractmethod
    def pattern(self: SelfValidator) -> str:
        """
        The regular expression that will be validated.

        :return: Regular expression.
        :rtype: str
        """

    @property
    @abstractmethod
    def minimum_length(self: SelfValidator) -> int:
        """
        The minimum token length required to start validation.

        :return: Minimum token length.
        :rtype: int
        """

    @abstractmethod
    def validate(self: SelfValidator) -> bool:
        """
        Validation logic.

        :return: `True` if validation is success. Otherwise `False`.
        :rtype: bool
        """

    @property
    @abstractmethod
    def error_message(self: SelfValidator) -> str:
        """
        The rule that the validator checked.

        :return: FDS rule.
        :rtype: str
        """


class BaseValidator(Validator):
    """Base validator."""

    def validate_length(self: SelfBaseValidator) -> bool:
        """
        Check for minimum token length.

        :return: `True` if the minimum length is less than specified and there is no separator.
                 Otherwise `False`.
        :rtype: bool
        """
        if (
            (len(self.number.cleaned_token) < self.minimum_length)
            and (SEPARATOR in self.number.token)
        ):
            return False

        return True

    def validate_token_as_int(self: SelfBaseValidator) -> bool:
        """
        Attempt to convert token to int.

        :return: `True` if operation is success. Otherwise `False`.
        :rtype: bool
        """
        try:
            int(self.number.token, self.number.numeral_system.value)
        except ValueError:
            return False

        return True


class NumberWithPrefixValidator(BaseValidator):
    """
    Validator for numbers with prefix.

    Specific validators for numbers with prefix should be inherited from this class.
    """
    def validate(self: SelfNumberWithPrefixValidator) -> bool:
        """
        Validating numbers with a prefix.

        1. Check the minimum length of the number token.
        2. Try to convert to `int`.
        3. Check by pattern.

        :return: `True` if all restrictions have been passed. Otherwise `False`.
        :rtype: bool
        """
        if not self.validate_length():
            return False
        if not self.validate_token_as_int():
            return False
        if not self.number.token.startswith(self.number.prefix.value):
            return False

        if len(self.number.cleaned_token) >= self.minimum_length:
            if not re.fullmatch(self.pattern, self.number.token[3:]):
                return False

        return True

    @property
    def number(self: SelfNumberWithPrefixValidator) -> NumberWithPrefix:
        """FDS Number with prefix."""
        raise NotImplementedError('A number with a prefix must be specified.')


class NumberWithOutPrefixValidator(BaseValidator):
    """
    Validator for numbers without prefix.

    Specific validators for numbers without prefix should be inherited from this class.
    """


class BaseDecimalValidator(NumberWithOutPrefixValidator):
    """Base validator for decimal numbers."""

    def validate_token_as_float(self: SelfBaseDecimalValidator) -> bool:
        """
        Attempt to convert token to float.

        :return: `True` if operation is success. Otherwise `False`.
        :rtype: bool
        """
        try:
            float(self.number.token)
        except ValueError:
            return False

        return True

    def validate_token_as_int(self: SelfBaseDecimalValidator) -> NoReturn:
        raise TypeError('Token cannot be converted to `int`."')
