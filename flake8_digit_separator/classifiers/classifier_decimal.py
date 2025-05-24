from typing import TypeVar

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.classifiers.types import TokenLikeStr
from flake8_digit_separator.fds_numbers.enums import NumberDelimiter
from flake8_digit_separator.fds_numbers.fds_numbers import DecimalNumber

SelfDecimalClassifier = TypeVar('SelfDecimalClassifier', bound='DecimalClassifier')


class DecimalClassifier(BaseClassifier):
    def __init__(self: SelfDecimalClassifier, token: TokenLikeStr) -> None:
        self._token = token

    def classify(self: SelfDecimalClassifier) -> DecimalNumber | None:
        if NumberDelimiter.DECIMAL.value in self.token:
            return DecimalNumber(self.token)

    @property
    def token(self: SelfDecimalClassifier) -> TokenLikeStr:
        return self._token
