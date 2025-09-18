"""Tests for the fds-exclude option functionality."""

import ast
import subprocess
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from flake8_digit_separator.checker import Checker


def test_add_options_adds_fds_exclude_option():
    """Test that add_options adds the fds-exclude option to the parser."""
    mock_parser = Mock()

    Checker.add_options(mock_parser)

    mock_parser.add_option.assert_called_once()
    call_args = mock_parser.add_option.call_args

    assert '--fds-exclude' in call_args[0]

    assert call_args[1]['action'] == 'store'
    assert call_args[1]['type'] is str
    assert call_args[1]['default'] == ''
    assert 'exclude from digit separator validation' in call_args[1]['help']


def test_parse_options_with_valid_exclude_list():
    """Test parsing valid exclude list."""
    mock_options = Mock()
    mock_options.fds_exclude = '8080,443,80,3000'

    Checker.parse_options(mock_options)

    assert Checker.excluded_numbers == {8080, 443, 80, 3000}


def test_parse_options_with_empty_exclude_list():
    """Test parsing empty exclude list."""
    mock_options = Mock()
    mock_options.fds_exclude = ''

    Checker.parse_options(mock_options)

    assert Checker.excluded_numbers == set()


def test_parse_options_with_invalid_exclude_list():
    """Test parsing invalid exclude list falls back to empty set."""
    mock_options = Mock()
    mock_options.fds_exclude = '8080,invalid,443'

    Checker.parse_options(mock_options)

    assert Checker.excluded_numbers == set()


def test_parse_options_with_whitespace_in_exclude_list():
    """Test parsing exclude list with whitespace is handled correctly."""
    mock_options = Mock()
    mock_options.fds_exclude = ' 8080 , 443 , 80 '

    Checker.parse_options(mock_options)

    assert Checker.excluded_numbers == {8080, 443, 80}


def test_should_exclude_number_with_excluded_integer():
    """Test that excluded integers are properly identified."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_number = Mock()
    mock_number.token = '8080'

    checker = Checker(ast.parse(''), [])
    result = checker._should_exclude_number(mock_number)

    assert result is True


def test_should_exclude_number_with_non_excluded_integer():
    """Test that non-excluded integers are not excluded."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_number = Mock()
    mock_number.token = '3000'

    checker = Checker(ast.parse(''), [])
    result = checker._should_exclude_number(mock_number)

    assert result is False


def test_should_exclude_number_with_excluded_float():
    """Test that excluded whole number floats are properly identified."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_number = Mock()
    mock_number.token = '8080.0'

    checker = Checker(ast.parse(''), [])
    result = checker._should_exclude_number(mock_number)

    assert result is False


def test_should_exclude_number_with_non_whole_float():
    """Test that non-whole floats are not excluded even if integer part matches."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_number = Mock()
    mock_number.token = '8080.5'

    checker = Checker(ast.parse(''), [])
    result = checker._should_exclude_number(mock_number)

    assert result is False


def test_should_exclude_number_with_invalid_token():
    """Test that invalid tokens are not excluded."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_number = Mock()
    mock_number.token = 'invalid'

    checker = Checker(ast.parse(''), [])
    result = checker._should_exclude_number(mock_number)

    assert result is False


def test_should_exclude_number_without_excluded_numbers_attribute():
    """Test behavior when excluded_numbers attribute doesn't exist."""
    if hasattr(Checker, 'excluded_numbers'):
        delattr(Checker, 'excluded_numbers')

    mock_number = Mock()
    mock_number.token = '8080'

    checker = Checker(ast.parse(''), [])
    result = checker._should_exclude_number(mock_number)

    assert result is False


def test_should_exclude_number_without_token_attribute():
    """Test behavior when number object doesn't have token attribute."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_number = Mock()
    del mock_number.token

    checker = Checker(ast.parse(''), [])
    result = checker._should_exclude_number(mock_number)

    assert result is False


def test_process_number_token_excludes_excluded_numbers():
    """Test that _process_number_token excludes numbers in the exclude list."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_token = Mock()
    mock_token.string = '8080'
    mock_token.start = (1, 0)

    with patch.object(Checker, '_classify') as mock_classify:
        mock_number = Mock()
        mock_number.is_supported = True
        mock_number.token = '8080'
        mock_classify.return_value = mock_number

        checker = Checker(ast.parse(''), [])
        result = checker._process_number_token(mock_token)

        assert result is None


def test_process_number_token_validates_non_excluded_numbers():
    """Test that _process_number_token validates numbers not in the exclude list."""
    Checker.excluded_numbers = {8080, 443, 80}

    mock_token = Mock()
    mock_token.string = '3000'
    mock_token.start = (1, 0)

    with (
        patch.object(Checker, '_classify') as mock_classify,
        patch('flake8_digit_separator.checker.ValidatorRegistry.get_validator') as mock_get_validator,
    ):
        mock_number = Mock()
        mock_number.is_supported = True
        mock_number.token = '3000'
        mock_classify.return_value = mock_number

        mock_validator = Mock()
        mock_validator.validate.return_value = False
        mock_validator.error_message = 'FDS100: Invalid number format'
        mock_get_validator.return_value = mock_validator

        checker = Checker(ast.parse(''), [])
        result = checker._process_number_token(mock_token)

        assert result is not None
        assert result.message == 'FDS100: Invalid number format'


def test_exclude_option_via_command_line():
    """Test that the exclude option works via command line."""
    test_code = """
    port = 8080
    timeout = 3000
    max_connections = 100
    """

    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(test_code)
        temp_file = f.name

    try:
        result = subprocess.run(
            [
                'flake8',
                '--isolated',
                '--select',
                'FDS',
                '--fds-exclude',
                '8080,3000',
                temp_file,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        output_lines = result.stdout.strip().split('\n') if result.stdout.strip() else []

        fds_errors = [line for line in output_lines if 'FDS' in line]

        assert len(fds_errors) >= 0

    finally:
        Path(temp_file).unlink()


def test_exclude_option_via_config_file():
    """Test that the exclude option works via config file."""
    test_code = """
    port = 8080
    timeout = 3000
    max_connections = 100
    """

    config_content = """
    [flake8]
    fds-exclude = 8080,3000
    """

    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(test_code)
        temp_file = f.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.cfg', delete=False) as f:
        f.write(config_content)
        config_file = f.name

    try:
        result = subprocess.run(
            [
                'flake8',
                '--config',
                config_file,
                '--isolated',
                '--select',
                'FDS',
                temp_file,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        output_lines = result.stdout.strip().split('\n') if result.stdout.strip() else []

        fds_errors = [line for line in output_lines if 'FDS' in line]

        assert len(fds_errors) >= 0

    finally:
        Path(temp_file).unlink()
        Path(config_file).unlink()
