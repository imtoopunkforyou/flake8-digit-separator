from typing import TypeVar

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.enums import NumberPrefix
from flake8_digit_separator.fds_numbers.fds_numbers import OctalNumber
from flake8_digit_separator.types import TokenLikeStr

SelfOctalClassifier = TypeVar('SelfOctalClassifier', bound='OctalClassifier')


class OctalClassifier(BaseClassifier):
    def __init__(self: SelfOctalClassifier, token: TokenLikeStr) -> None:
        self._token = token

    def classify(self: SelfOctalClassifier) -> OctalNumber:
        if self.token_lower.startswith(NumberPrefix.OCTAL.value):
            return OctalNumber(self.token_lower)

    @property
    def token(self: SelfOctalClassifier) -> TokenLikeStr:
        return self._token
