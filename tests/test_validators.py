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
        # Create a binary number with invalid token
        binary_number = BinaryNumber(
            token='0binvalid',  # Invalid binary token that can't be converted to int  # noqa: S106
        )

        validator = BinaryValidator(binary_number)

        # Should return False when validate_token_as_int fails
        assert validator.validate() is False


class TestFloatValidator:
    """Test FloatValidator class."""

    def test_validate_returns_false_for_invalid_float(self):
        """Test that validate returns False when validate_token_as_float fails."""
        # Create a float number with invalid token
        float_number = FloatNumber(
            token='invalid_float',  # Invalid float token that can't be converted to float  # noqa: S106
        )

        validator = FloatValidator(float_number)

        # Should return False when validate_token_as_float fails
        assert validator.validate() is False


class TestHexValidator:
    """Test HexValidator class."""

    def test_validate_returns_false_for_invalid_hex_int(self):
        """Test that validate returns False when validate_token_as_int fails."""
        # Create a hex number with invalid token
        hex_number = HexNumber(
            token='0xinvalid',  # Invalid hex token that can't be converted to int  # noqa: S106
        )

        validator = HexValidator(hex_number)

        # Should return False when validate_token_as_int fails
        assert validator.validate() is False


class TestIntValidator:
    """Test IntValidator class."""

    def test_validate_returns_false_for_invalid_int(self):
        """Test that validate returns False when validate_token_as_int fails."""
        # Create an int number with invalid token
        int_number = IntNumber(
            token='invalid_int',  # Invalid int token that can't be converted to int  # noqa: S106
        )

        validator = IntValidator(int_number)

        # Should return False when validate_token_as_int fails
        assert validator.validate() is False


class TestOctalValidator:
    """Test OctalValidator class."""

    def test_validate_returns_false_for_invalid_octal_int(self):
        """Test that validate returns False when validate_token_as_int fails."""
        # Create an octal number with invalid token
        octal_number = OctalNumber(
            token='0oinvalid',  # Invalid octal token that can't be converted to int  # noqa: S106
        )

        validator = OctalValidator(octal_number)

        # Should return False when validate_token_as_int fails
        assert validator.validate() is False
