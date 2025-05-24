from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.numbers.numbers import ScientificNumber


class ScientifiClassifier(BaseClassifier):
    def __init__(self, token: str) -> None:
        self._token = token

    def classify(self) -> ScientificNumber | None:
        if 'e' in self.token_lower:
            return ScientificNumber(self.token_lower)

    @property
    def token(self) -> str:
        return self._token
