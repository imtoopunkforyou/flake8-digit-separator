import pytest

from flake8_digit_separator.fds_numbers.base import FDSNumber
from flake8_digit_separator.fds_numbers.enums import NumeralSystem
from flake8_digit_separator.validators.registry import ValidatorRegistry


class UnknownNumber(FDSNumber):
    """Custom number class that has no registered validator."""
    pass


class TestValidatorRegistry:
    """Test ValidatorRegistry class."""

    def test_get_validator_raises_value_error_for_unknown_number_type(self):
        """Test that get_validator raises ValueError for unknown number types."""
        # Create an unknown number type
        unknown_number = UnknownNumber(
            token="123",
            numeral_system=NumeralSystem.FLOAT,
            is_supported=True
        )
        
        # Should raise ValueError when no validator is registered
        with pytest.raises(ValueError, match="No validator registered for"):
            ValidatorRegistry.get_validator(unknown_number) 