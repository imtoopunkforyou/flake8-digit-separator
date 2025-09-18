from flake8_digit_separator.classifiers.classifier_binary import BinaryClassifier
from flake8_digit_separator.classifiers.classifier_complex import ComplexClassifier
from flake8_digit_separator.classifiers.classifier_float import FloatClassifier
from flake8_digit_separator.classifiers.classifier_hex import HexClassifier
from flake8_digit_separator.classifiers.classifier_octal import OctalClassifier


class TestBinaryClassifier:
    """Test BinaryClassifier class."""

    def test_classify_returns_binary_number_for_valid_binary(self):
        """Test that classify returns BinaryNumber for valid binary tokens."""
        classifier = BinaryClassifier('0b_1101_1001')
        result = classifier.classify()

        assert result is not None
        assert result.token == '0b_1101_1001'

    def test_classify_returns_none_for_invalid_binary(self):
        """Test that classify returns None for invalid binary tokens."""
        classifier = BinaryClassifier('0x_CAFE')
        result = classifier.classify()

        assert result is None

    def test_token_property(self):
        """Test that token property returns the correct value."""
        classifier = BinaryClassifier('0b_1101_1001')
        assert classifier.token == '0b_1101_1001'


class TestComplexClassifier:
    """Test ComplexClassifier class."""

    def test_classify_returns_complex_number_for_valid_complex(self):
        """Test that classify returns ComplexNumber for valid complex tokens."""
        classifier = ComplexClassifier('1+2j')
        result = classifier.classify()

        assert result is not None
        assert result.token == '1+2j'

    def test_classify_returns_none_for_invalid_complex(self):
        """Test that classify returns None for invalid complex tokens."""
        classifier = ComplexClassifier('123')
        result = classifier.classify()

        assert result is None

    def test_token_property(self):
        """Test that token property returns the correct value."""
        classifier = ComplexClassifier('1+2j')
        assert classifier.token == '1+2j'


class TestFloatClassifier:
    """Test FloatClassifier class."""

    def test_classify_returns_float_number_for_valid_float(self):
        """Test that classify returns FloatNumber for valid float tokens."""
        classifier = FloatClassifier('10.5')
        result = classifier.classify()

        assert result is not None
        assert result.token == '10.5'

    def test_classify_returns_none_for_invalid_float(self):
        """Test that classify returns None for invalid float tokens."""
        classifier = FloatClassifier('123')
        result = classifier.classify()

        assert result is None

    def test_token_property(self):
        """Test that token property returns the correct value."""
        classifier = FloatClassifier('10.5')
        assert classifier.token == '10.5'


class TestHexClassifier:
    """Test HexClassifier class."""

    def test_classify_returns_hex_number_for_valid_hex(self):
        """Test that classify returns HexNumber for valid hex tokens."""
        classifier = HexClassifier('0x_CAFE_F00D')
        result = classifier.classify()

        assert result is not None
        assert result.token == '0x_cafe_f00d'  # Should be lowercased

    def test_classify_returns_none_for_invalid_hex(self):
        """Test that classify returns None for invalid hex tokens."""
        classifier = HexClassifier('123')
        result = classifier.classify()

        assert result is None

    def test_token_property(self):
        """Test that token property returns the correct value."""
        classifier = HexClassifier('0x_CAFE_F00D')
        assert classifier.token == '0x_CAFE_F00D'


class TestOctalClassifier:
    """Test OctalClassifier class."""

    def test_classify_returns_octal_number_for_valid_octal(self):
        """Test that classify returns OctalNumber for valid octal tokens."""
        classifier = OctalClassifier('0o_12_134_155')
        result = classifier.classify()

        assert result is not None
        assert result.token == '0o_12_134_155'

    def test_classify_returns_none_for_invalid_octal(self):
        """Test that classify returns None for invalid octal tokens."""
        classifier = OctalClassifier('123')
        result = classifier.classify()

        assert result is None

    def test_token_property(self):
        """Test that token property returns the correct value."""
        classifier = OctalClassifier('0o_12_134_155')
        assert classifier.token == '0o_12_134_155'
