from flake8_digit_separator.classifiers.base import BaseClassifier
from flake8_digit_separator.fds_numbers.enums import NumberPrefix
from flake8_digit_separator.fds_numbers.fds_numbers import OctalNumber


class OctalClassifier(BaseClassifier):
    def __init__(self, token: str) -> None:
        self._token = token

    def classify(self) -> OctalNumber:
        if self.token_lower.startswith(NumberPrefix.OCTAL.value):
            return OctalNumber(self.token_lower)

    @property
    def token(self) -> str:
        return self._token
