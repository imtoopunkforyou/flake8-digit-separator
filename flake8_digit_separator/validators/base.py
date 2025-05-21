from abc import ABC, abstractmethod
from typing import ClassVar

from validators.enums import NumberDelimiter, NumberPrefix, NumeralSystem

from flake8_digit_separator.validators.numbers import Number


class BaseClassifier(ABC):
    @abstractmethod
    def classify(self):
        ...


class Validator(ABC):
    @property
    @abstractmethod
    def number(self) -> Number:
        ...

    def validate_supported(self) -> bool:
        return self.number.supported

    def validate_token_as_int(self):
        try:
            int(self.number.token, self.number.numeral_system)
        except ValueError:
            return False

        return True

    @property
    @abstractmethod
    def slice_size(self):
        ...

    @property
    @abstractmethod
    def pattern(self) -> str:
        ...

    @abstractmethod
    def validate(self):
        ...

    @property
    @abstractmethod
    def error_message(self):
        ...




# class NumberValidator(Number, Validator, Cleaner):
#     pass


# class NumberWithPrefixValidator(NumberWithPrefix, Validator, Cleaner):
#     pass


# class NumberWithDelimiterValidator(NumberWithDelimiter, Validator, Cleaner):
#     pass


# class NumberValidatorsFactory(ABC):
#     @property
#     @abstractmethod
#     def token(self):
#         ...

#     @abstractmethod
#     def create_ordered_classifiers(self) -> tuple[NumberValidator, ...]:
#         ...

