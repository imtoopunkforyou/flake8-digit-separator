from flake8_digit_separator.fds_numbers.fds_numbers import (
    BinaryNumber,
    FloatNumber,
    HexNumber,
    IntNumber,
    OctalNumber,
)
from flake8_digit_separator.validators.validator_binary import BinaryValidator
from flake8_digit_separator.validators.validator_float import FloatValidator
from flake8_digit_separator.validators.validator_hex import HexValidator
from flake8_digit_separator.validators.validator_int import IntValidator
from flake8_digit_separator.validators.validator_octal import OctalValidator


class TestBinaryValidator:
    """Test BinaryValidator class."""

    def test_validate_returns_false_for_invalid_binary_int(self):
        """Test that validate returns False when validate_token_as_int fails."""
        binary_number = BinaryNumber(
            token='0binvalid',  # Invalid binary token that can't be converted to int
        )

        validator = BinaryValidator(binary_number)

        assert validator.validate() is False

    def test_pattern_property(self):
        """Test that pattern property returns the correct regex."""
        binary_number = BinaryNumber(token='0b_1101_1001')
        validator = BinaryValidator(binary_number)

        expected_pattern = r'^[+-]?0[bB]_([01]{1,4}(_[01]{4})*)$'
        assert validator.pattern == expected_pattern

    def test_error_message_property(self):
        """Test that error_message property returns the correct message."""
        binary_number = BinaryNumber(token='0b_1101_1001')
        validator = BinaryValidator(binary_number)

        error_message = validator.error_message
        assert 'FDS300' in error_message
        assert 'Group by 4s from right after prefix' in error_message


class TestFloatValidator:
    """Test FloatValidator class."""

    def test_validate_returns_false_for_invalid_float(self):
        """Test that validate returns False when validate_token_as_float fails."""
        float_number = FloatNumber(
            token='invalid_float',  # Invalid float token that can't be converted to float
        )

        validator = FloatValidator(float_number)

        assert validator.validate() is False

    def test_pattern_property(self):
        """Test that pattern property returns the correct regex."""
        float_number = FloatNumber(token='10_000.1_234')
        validator = FloatValidator(float_number)

        expected_pattern = r'^[+-]?(?:(?!0_)\d{1,3}(?:_\d{3})*\.\d{1,3}(?:_\d{3})*|\.\d{1,3}(?:_\d{3})*)$'
        assert validator.pattern == expected_pattern

    def test_error_message_property(self):
        """Test that error_message property returns the correct message."""
        float_number = FloatNumber(token='10_000.1_234')
        validator = FloatValidator(float_number)

        error_message = validator.error_message
        assert 'FDS200' in error_message
        assert 'Group by 3s from right' in error_message


class TestHexValidator:
    """Test HexValidator class."""

    def test_validate_returns_false_for_invalid_hex_int(self):
        """Test that validate returns False when validate_token_as_int fails."""
        hex_number = HexNumber(
            token='0xinvalid',  # Invalid hex token that can't be converted to int
        )

        validator = HexValidator(hex_number)

        assert validator.validate() is False

    def test_pattern_property(self):
        """Test that pattern property returns the correct regex."""
        hex_number = HexNumber(token='0x_CAFE_F00D')
        validator = HexValidator(hex_number)

        expected_pattern = r'^[+-]?0[xX]_[0-9a-fA-F]{1,4}(?:_[0-9a-fA-F]{4})*$'
        assert validator.pattern == expected_pattern

    def test_error_message_property(self):
        """Test that error_message property returns the correct message."""
        hex_number = HexNumber(token='0x_CAFE_F00D')
        validator = HexValidator(hex_number)

        error_message = validator.error_message
        assert 'FDS500' in error_message
        assert 'Group by 4s from right after prefix' in error_message


class TestIntValidator:
    """Test IntValidator class."""

    def test_validate_returns_false_for_invalid_int(self):
        """Test that validate returns False when validate_token_as_int fails."""
        int_number = IntNumber(
            token='invalid_int',  # Invalid int token that can't be converted to int
        )

        validator = IntValidator(int_number)

        assert validator.validate() is False

    def test_pattern_property(self):
        """Test that pattern property returns the correct regex."""
        int_number = IntNumber(token='10_000')
        validator = IntValidator(int_number)

        expected_pattern = r'^[+-]?(?!0_)\d{1,3}(?:_\d{3})*$'
        assert validator.pattern == expected_pattern

    def test_error_message_property(self):
        """Test that error_message property returns the correct message."""
        int_number = IntNumber(token='10_000')
        validator = IntValidator(int_number)

        error_message = validator.error_message
        assert 'FDS100' in error_message
        assert 'Group by 3s from right' in error_message


class TestOctalValidator:
    """Test OctalValidator class."""

    def test_validate_returns_false_for_invalid_octal_int(self):
        """Test that validate returns False when validate_token_as_int fails."""
        octal_number = OctalNumber(
            token='0oinvalid',  # Invalid octal token that can't be converted to int
        )

        validator = OctalValidator(octal_number)

        assert validator.validate() is False

    def test_pattern_property(self):
        """Test that pattern property returns the correct regex."""
        octal_number = OctalNumber(token='0o_12_134_155')
        validator = OctalValidator(octal_number)

        expected_pattern = r'^[+-]?0[oO]_[0-7]{1,3}(_[0-7]{3})*$'
        assert validator.pattern == expected_pattern

    def test_error_message_property(self):
        """Test that error_message property returns the correct message."""
        octal_number = OctalNumber(token='0o_12_134_155')
        validator = OctalValidator(octal_number)

        error_message = validator.error_message
        assert 'FDS400' in error_message
        assert 'Group by 3s from right after prefix' in error_message
