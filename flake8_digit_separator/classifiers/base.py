from abc import ABC, abstractmethod
from typing import TypeAlias, TypeVar

from flake8_digit_separator.classifiers.types import TokenLikeStr
from flake8_digit_separator.fds_numbers.base import FDSNumber

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
    def classify(self: SelfClassifier) -> FDSNumber:
        ...


class BaseClassifier(Classifier):
    @property
    def token_lower(self) -> LowerTokenLikeStr:
        return self.token.lower()
