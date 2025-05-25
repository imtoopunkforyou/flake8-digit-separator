from typing import TypeVar, final

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.classifiers.types import TokenLikeStr
from flake8_digit_separator.fds_numbers.enums import NumberPrefix
from flake8_digit_separator.fds_numbers.fds_numbers import HexNumber

SelfHexClassifier = TypeVar('SelfHexClassifier', bound='HexClassifier')


@final
class HexClassifier(BaseClassifier):
    def __init__(
        self: SelfHexClassifier,
        token: TokenLikeStr,
    ) -> None:
        self._token = token

    def classify(self: SelfHexClassifier) -> HexNumber:
        if self.token_lower.startswith(NumberPrefix.HEX.value):
            return HexNumber(self.token_lower)

    @property
    def token(self: SelfHexClassifier) -> TokenLikeStr:
        return self._token
