from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.fds_numbers import IntNumber


class IntClassifier(BaseClassifier):
    def __init__(self, token: str) -> None:
        self._token = token

    def classify(self) -> IntNumber:
        return IntNumber(self.token)

    @property
    def token(self) -> str:
        return self._token
