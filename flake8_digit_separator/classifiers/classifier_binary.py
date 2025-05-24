from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.enums import NumberPrefix
from flake8_digit_separator.fds_numbers.fds_numbers import BinaryNumber


class BinaryClassifier(BaseClassifier):
    def __init__(self, token: str) -> None:
        self._token = token

    def classify(self) -> BinaryNumber | None:
        if self.token_lower.startswith(NumberPrefix.BINARY.value):
            return BinaryNumber(self.token_lower)

    @property
    def token(self) -> str:
        return self._token
