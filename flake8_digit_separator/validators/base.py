from abc import ABC, abstractmethod

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

    def validate_token_as_int(self):
        try:
            int(self.number.token, self.number.numeral_system)
        except ValueError:
            return False

        return True

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
