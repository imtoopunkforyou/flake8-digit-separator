from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.numbers.enums import NumberPrefix
from flake8_digit_separator.numbers.numbers import HexNumber


class HexClassifier(BaseClassifier):
    def __init__(self, token: str) -> None:
        self._token = token

    def classify(self) -> HexNumber:
        if self.token_lower.startswith(NumberPrefix.HEX.value):
            return HexNumber(self.token_lower)

    @property
    def token(self) -> str:
        return self._token
