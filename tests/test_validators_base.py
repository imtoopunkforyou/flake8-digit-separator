from unittest.mock import patch

from flake8_digit_separator.fds_numbers.base import FDSNumber
from flake8_digit_separator.fds_numbers.enums import NumeralSystem
from flake8_digit_separator.validators.base import BaseValidator


class ConcreteValidator(BaseValidator):
    """Test implementation of BaseValidator."""

    def __init__(self, number) -> None:
        self._number = number

    @property
    def number(self):
        return self._number

    @property
    def pattern(self):
        return r'.*'

    def validate(self):
        return True

    @property
    def error_message(self):
        return 'Test error'


class TestValidateTokenAsInt:
    """Test validate_token_as_int method."""

    def test_validate_token_as_int_with_invalid_token_returns_false(self):
        """Test that validate_token_as_int returns False for invalid tokens."""
        # Create a number with invalid token for int conversion
        number = FDSNumber(
            token='invalid_int',  # noqa: S106
            numeral_system=NumeralSystem.FLOAT,
            is_supported=True,
        )

        validator = ConcreteValidator(number)

        # Should return False for invalid int token
        assert validator.validate_token_as_int() is False

    @patch('flake8_digit_separator.validators.base.int')
    def test_validate_token_as_int_with_invalid_base_returns_false(self, mock_int):
        """Test that validate_token_as_int returns False for invalid base."""
        # Mock int() to raise ValueError
        mock_int.side_effect = ValueError('invalid base')

        # Create a number with any valid parameters
        number = FDSNumber(
            token='12345',  # noqa: S106
            numeral_system=NumeralSystem.HEX,
            is_supported=True,
        )

        validator = ConcreteValidator(number)

        # Should return False when int() raises ValueError
        assert validator.validate_token_as_int() is False


class TestValidateTokenAsFloat:
    """Test validate_token_as_float method."""

    def test_validate_token_as_float_with_invalid_token_returns_false(self):
        """Test that validate_token_as_float returns False for invalid tokens."""
        # Create a number with invalid token for float conversion
        number = FDSNumber(
            token='invalid_float',  # noqa: S106
            numeral_system=NumeralSystem.FLOAT,
            is_supported=True,
        )

        validator = ConcreteValidator(number)

        # Should return False for invalid float token
        assert validator.validate_token_as_float() is False

    def test_validate_token_as_float_with_complex_number_returns_false(self):
        """Test that validate_token_as_float returns False for complex numbers."""
        # Create a number with complex number token
        number = FDSNumber(
            token='1+2j',  # Complex number that can't be converted to float  # noqa: S106
            numeral_system=NumeralSystem.FLOAT,
            is_supported=True,
        )

        validator = ConcreteValidator(number)

        # Should return False for complex number
        assert validator.validate_token_as_float() is False
