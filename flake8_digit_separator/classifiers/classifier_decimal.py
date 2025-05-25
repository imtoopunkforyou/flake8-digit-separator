from typing import TypeVar, final

from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.classifiers.types import TokenLikeStr
from flake8_digit_separator.fds_numbers.enums import NumberDelimiter
from flake8_digit_separator.fds_numbers.fds_numbers import DecimalNumber

SelfDecimalClassifier = TypeVar('SelfDecimalClassifier', bound='DecimalClassifier')


@final
class DecimalClassifier(BaseClassifier):
    """Classifier for decimal numbers."""

    def __init__(
        self: SelfDecimalClassifier,
        token: TokenLikeStr,
    ) -> None:
        self._token = token

    def classify(self: SelfDecimalClassifier) -> DecimalNumber | None:
        """
        Returns a decimal number if it matches.

        :return: Decimal number
        :rtype: DecimalNumber | None
        """
        if NumberDelimiter.DECIMAL.value in self.token:
            return DecimalNumber(self.token)

        return None

    @property
    def token(self: SelfDecimalClassifier) -> TokenLikeStr:
        """
        Token string from `tokenize.TokenInfo` object.

        :return: Token like string.
        :rtype: TokenLikeStr
        """
        return self._token
