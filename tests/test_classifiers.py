from flake8_digit_separator.classifiers.classifier_binary import BinaryClassifier
from flake8_digit_separator.classifiers.classifier_complex import ComplexClassifier
from flake8_digit_separator.classifiers.classifier_float import FloatClassifier
from flake8_digit_separator.classifiers.classifier_hex import HexClassifier
from flake8_digit_separator.classifiers.classifier_octal import OctalClassifier


def test_binary_classify_returns_binary_number_for_valid_binary():
    """Test that classify returns BinaryNumber for valid binary tokens."""
    classifier = BinaryClassifier('0b_1101_1001')
    result = classifier.classify()

    assert result is not None
    assert result.token == '0b_1101_1001'


def test_binary_classify_returns_none_for_invalid_binary():
    """Test that classify returns None for invalid binary tokens."""
    classifier = BinaryClassifier('0x_CAFE')
    result = classifier.classify()

    assert result is None


def test_binary_token_property():
    """Test that token property returns the correct value."""
    classifier = BinaryClassifier('0b_1101_1001')
    assert classifier.token == '0b_1101_1001'


def test_complex_classify_returns_complex_number_for_valid_complex():
    """Test that classify returns ComplexNumber for valid complex tokens."""
    classifier = ComplexClassifier('1+2j')
    result = classifier.classify()

    assert result is not None
    assert result.token == '1+2j'


def test_complex_classify_returns_none_for_invalid_complex():
    """Test that classify returns None for invalid complex tokens."""
    classifier = ComplexClassifier('123')
    result = classifier.classify()

    assert result is None


def test_complex_token_property():
    """Test that token property returns the correct value."""
    classifier = ComplexClassifier('1+2j')
    assert classifier.token == '1+2j'


def test_float_classify_returns_float_number_for_valid_float():
    """Test that classify returns FloatNumber for valid float tokens."""
    classifier = FloatClassifier('10.5')
    result = classifier.classify()

    assert result is not None
    assert result.token == '10.5'


def test_float_classify_returns_none_for_invalid_float():
    """Test that classify returns None for invalid float tokens."""
    classifier = FloatClassifier('123')
    result = classifier.classify()

    assert result is None


def test_float_token_property():
    """Test that token property returns the correct value."""
    classifier = FloatClassifier('10.5')
    assert classifier.token == '10.5'


def test_hex_classify_returns_hex_number_for_valid_hex():
    """Test that classify returns HexNumber for valid hex tokens."""
    classifier = HexClassifier('0x_CAFE_F00D')
    result = classifier.classify()

    assert result is not None
    assert result.token == '0x_cafe_f00d'


def test_hex_classify_returns_none_for_invalid_hex():
    """Test that classify returns None for invalid hex tokens."""
    classifier = HexClassifier('123')
    result = classifier.classify()

    assert result is None


def test_hex_token_property():
    """Test that token property returns the correct value."""
    classifier = HexClassifier('0x_CAFE_F00D')
    assert classifier.token == '0x_CAFE_F00D'


def test_octal_classify_returns_octal_number_for_valid_octal():
    """Test that classify returns OctalNumber for valid octal tokens."""
    classifier = OctalClassifier('0o_12_134_155')
    result = classifier.classify()

    assert result is not None
    assert result.token == '0o_12_134_155'


def test_octal_classify_returns_none_for_invalid_octal():
    """Test that classify returns None for invalid octal tokens."""
    classifier = OctalClassifier('123')
    result = classifier.classify()

    assert result is None


def test_octal_token_property():
    """Test that token property returns the correct value."""
    classifier = OctalClassifier('0o_12_134_155')
    assert classifier.token == '0o_12_134_155'
