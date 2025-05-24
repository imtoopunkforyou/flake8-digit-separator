from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.numbers.enums import NumberDelimiter
from flake8_digit_separator.numbers.numbers import DecimalNumber


class DecimalClassifier(BaseClassifier):
    def __init__(self, token: str) -> None:
        self._token = token

    def classify(self) -> DecimalNumber | None:
        if NumberDelimiter.DECIMAL.value in self.token:
            return DecimalNumber(self.token)

    @property
    def token(self) -> str:
        return self._token
