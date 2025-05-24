from typing import TypeVar

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.fds_numbers import IntNumber
from flake8_digit_separator.types import TokenLikeStr

SelfIntClassifier = TypeVar('SelfIntClassifier', bound='IntClassifier')


class IntClassifier(BaseClassifier):
    def __init__(self: SelfIntClassifier, token: TokenLikeStr) -> None:
        self._token = token

    def classify(self: SelfIntClassifier) -> IntNumber:
        return IntNumber(self.token)

    @property
    def token(self) -> TokenLikeStr:
        return self._token
