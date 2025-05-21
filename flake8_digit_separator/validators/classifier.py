from flake8_digit_separator.validators.base import BaseClassifier
from flake8_digit_separator.validators.enums import (
    NumberDelimiter,
    NumberPrefix,
)
from flake8_digit_separator.validators.numbers import (
    BinaryNumber,
    ComplexNumber,
    DecimalNumber,
    HexNumber,
    IntNumber,
    Number,
    OctalNumber,
    ScientificNumber,
)


class Classifier(BaseClassifier):
    def classify(self, token: str) -> Number:  # noqa: WPS212
        token = token.lower()
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
