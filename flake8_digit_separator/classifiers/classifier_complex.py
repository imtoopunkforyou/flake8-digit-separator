from typing import TypeVar

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.fds_numbers import ComplexNumber
from flake8_digit_separator.types import TokenLikeStr

SelfComplexClassifier = TypeVar('SelfComplexClassifier', bound='ComplexClassifier')


class ComplexClassifier(BaseClassifier):
    def __init__(self: SelfComplexClassifier, token: TokenLikeStr) -> None:
        self._token = token

    def classify(self: SelfComplexClassifier) -> ComplexNumber | None:
        if 'j' in self.token_lower:
            return ComplexNumber(self.token_lower)

    @property
    def token(self: SelfComplexClassifier) -> str:
        return self._token
