from abc import ABC, abstractmethod

from flake8_digit_separator.numbers.base import Number


class Classifier(ABC):
    @property
    @abstractmethod
    def token(self) -> str:
        ...

    @property
    @abstractmethod
    def token_lower(self):
        ...

    @abstractmethod
    def classify(self) -> Number:
        ...


class BaseClassifier(Classifier):
    @property
    def token_lower(self) -> str:
        return self.token.lower()
