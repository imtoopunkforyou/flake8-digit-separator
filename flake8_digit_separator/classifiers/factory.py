from flake8_digit_separator.classifiers.base import NumberValidatorsFactory
from flake8_digit_separator.classifiers.classifiers import (
    BinaryClassifier,
    # ComplexClassifier,
    DecimalClassifier,
    HexClassifier,
    IntClassifier,
    OctalClassifier,
    # ScientificClassifier,
)


class ClassifiersFactory(NumberValidatorsFactory):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    def create_ordered_classifiers(self):
        return (  # noqa: WPS227
            # ComplexClassifier(self.token),
            HexClassifier(self.token),
            BinaryClassifier(self.token),
            OctalClassifier(self.token),
            # ScientificClassifier(self.token),
            DecimalClassifier(self.token),
            IntClassifier(self.token),
        )
