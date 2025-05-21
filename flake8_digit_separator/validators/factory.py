from flake8_digit_separator.validators.base import NumberValidatorsFactory
from flake8_digit_separator.validators.validators import (
    BinaryClassifier,
    DecimalClassifier,
    HexClassifier,
    IntClassifier,
    OctalClassifier,
)


class ClassifiersFactory(NumberValidatorsFactory):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    def create_ordered_classifiers(self):
        return (
            HexClassifier(self.token),
            BinaryClassifier(self.token),
            OctalClassifier(self.token),
            DecimalClassifier(self.token),
            IntClassifier(self.token),
        )
