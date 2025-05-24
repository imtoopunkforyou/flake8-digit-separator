from typing import TypeVar

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.enums import NumberPrefix
from flake8_digit_separator.fds_numbers.fds_numbers import BinaryNumber
from flake8_digit_separator.types import TokenLikeStr

SelfBinaryClassifier = TypeVar('SelfBinaryClassifier', bound='BinaryClassifier')


class BinaryClassifier(BaseClassifier):
    def __init__(self: SelfBinaryClassifier, token: TokenLikeStr) -> None:
        self._token = token

    def classify(self: SelfBinaryClassifier) -> BinaryNumber | None:
        if self.token_lower.startswith(NumberPrefix.BINARY.value):
            return BinaryNumber(self.token_lower)

    @property
    def token(self: SelfBinaryClassifier) -> TokenLikeStr:
        return self._token
