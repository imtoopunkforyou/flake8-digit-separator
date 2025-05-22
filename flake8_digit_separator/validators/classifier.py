from flake8_digit_separator.numbers.base import Number
from flake8_digit_separator.numbers.numbers import (
    BinaryNumber,
    ComplexNumber,
    DecimalNumber,
    HexNumber,
    IntNumber,
    OctalNumber,
    ScientificNumber,
)
from flake8_digit_separator.validators.base import BaseClassifier
from flake8_digit_separator.validators.enums import (
    NumberDelimiter,
    NumberPrefix,
)


class Classifier(BaseClassifier):
    def __init__(self, token: str):
        self._token = token

    @property
    def token(self):
        return self._token

    def classify(self) -> Number:  # noqa: WPS212
        token = self._token.lower()
        match token:
            case tok if 'j' in tok:
                return ComplexNumber(tok)
            case tok if 'e' in tok:
                return ScientificNumber(tok)
            case tok if tok.startswith(NumberPrefix.BINARY.value):
                return BinaryNumber(tok)
            case tok if tok.startswith(NumberPrefix.HEX.value):
                return HexNumber(tok)
            case tok if tok.startswith(NumberPrefix.OCTAL.value):
                return OctalNumber(tok)
            case tok if NumberDelimiter.DECIMAL.value in tok:
                return DecimalNumber(tok)
            case _:
                return IntNumber(token)
