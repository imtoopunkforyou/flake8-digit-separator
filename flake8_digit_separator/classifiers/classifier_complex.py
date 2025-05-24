from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.numbers.numbers import ComplexNumber


class ComplexClassifier(BaseClassifier):
    def __init__(self, token: str) -> None:
        self._token = token

    def classify(self) -> ComplexNumber | None:
        if 'j' in self.token_lower:
            return ComplexNumber(self.token_lower)

    @property
    def token(self) -> str:
        return self._token
