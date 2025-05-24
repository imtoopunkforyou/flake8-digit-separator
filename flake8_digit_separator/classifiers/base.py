from abc import ABC, abstractmethod
from typing import TypeAlias, TypeVar

from flake8_digit_separator.fds_numbers.base import Number
from flake8_digit_separator.types import TokenLikeStr

SelfClassifier = TypeVar('SelfClassifier', bound='Classifier')

LowerTokenLikeStr: TypeAlias = str


class Classifier(ABC):
    @property
    @abstractmethod
    def token(self: SelfClassifier) -> TokenLikeStr:
        ...

    @property
    @abstractmethod
    def token_lower(self: SelfClassifier) -> LowerTokenLikeStr:
        ...

    @abstractmethod
    def classify(self: SelfClassifier) -> Number:
        ...


class BaseClassifier(Classifier):
    @property
    def token_lower(self) -> LowerTokenLikeStr:
        return self.token.lower()
