from typing import final

from flake8_digit_separator.classifiers.base import Classifier
from flake8_digit_separator.classifiers.classifier_binary import (
    BinaryClassifier,
)
from flake8_digit_separator.classifiers.classifier_complex import (
    ComplexClassifier,
)
from flake8_digit_separator.classifiers.classifier_decimal import (
    DecimalClassifier,
)
from flake8_digit_separator.classifiers.classifier_hex import HexClassifier
from flake8_digit_separator.classifiers.classifier_int import IntClassifier
from flake8_digit_separator.classifiers.classifier_octal import OctalClassifier
from flake8_digit_separator.classifiers.classifier_scientific import (
    ScientifiClassifier,
)


@final
class ClassifierRegistry:
    hex_classifier = HexClassifier
    octal_classifier = OctalClassifier
    binary_classifier = BinaryClassifier
    complex_classifier = ComplexClassifier
    scientific_classifier = ScientifiClassifier
    decimal_classifier = DecimalClassifier
    int_classifier = IntClassifier

    @classmethod
    def get_ordered_classifiers(cls) -> tuple[type[Classifier], ...]:
        return (  # noqa: WPS227
            cls.hex_classifier,
            cls.octal_classifier,
            cls.binary_classifier,
            cls.complex_classifier,
            cls.scientific_classifier,
            cls.decimal_classifier,
            cls.int_classifier,
        )
