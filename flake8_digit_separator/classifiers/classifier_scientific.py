from typing import TypeVar

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.fds_numbers import ScientificNumber
from flake8_digit_separator.types import TokenLikeStr

SelfScientifiClassifier = TypeVar('SelfScientifiClassifier', bound='ScientifiClassifier')


class ScientifiClassifier(BaseClassifier):
    def __init__(self: SelfScientifiClassifier, token: TokenLikeStr) -> None:
        self._token = token

    def classify(self: SelfScientifiClassifier) -> ScientificNumber | None:
        if 'e' in self.token_lower:
            return ScientificNumber(self.token_lower)

    @property
    def token(self) -> TokenLikeStr:
        return self._token
