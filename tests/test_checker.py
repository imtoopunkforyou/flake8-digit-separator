import ast
from unittest.mock import Mock, patch

from flake8_digit_separator.checker import Checker


class TestChecker:
    """Test Checker class."""

    @patch('flake8_digit_separator.checker.ClassifierRegistry.get_ordered_classifiers')
    def test_classify_returns_none_when_all_classifiers_return_none(self, mock_get_classifiers):
        """Test that _classify returns None when all classifiers return None."""
        mock_classifier_cls = Mock()
        mock_classifier_instance = Mock()
        mock_classifier_instance.classify.return_value = None
        mock_classifier_cls.return_value = mock_classifier_instance

        mock_get_classifiers.return_value = [mock_classifier_cls]

        mock_token = Mock()
        mock_token.string = 'some_token'

        checker = Checker(ast.parse(''), [])

        result = checker._classify(mock_token)

        assert result is None

    @patch('flake8_digit_separator.checker.ClassifierRegistry.get_ordered_classifiers')
    def test_classify_returns_none_when_all_classifiers_return_falsy(self, mock_get_classifiers):
        """Test that _classify returns None when all classifiers return falsy values."""
        mock_classifier1 = Mock()
        mock_instance1 = Mock()
        mock_instance1.classify.return_value = None
        mock_classifier1.return_value = mock_instance1

        mock_classifier2 = Mock()
        mock_instance2 = Mock()
        mock_instance2.classify.return_value = False
        mock_classifier2.return_value = mock_instance2

        mock_classifier3 = Mock()
        mock_instance3 = Mock()
        mock_instance3.classify.return_value = 0  # Falsy integer
        mock_classifier3.return_value = mock_instance3

        mock_get_classifiers.return_value = [mock_classifier1, mock_classifier2, mock_classifier3]

        mock_token = Mock()
        mock_token.string = 'some_token'

        checker = Checker(ast.parse(''), [])

        result = checker._classify(mock_token)

        assert result is None

    @patch('flake8_digit_separator.checker.ClassifierRegistry.get_ordered_classifiers')
    def test_classify_returns_none_when_no_classifiers(self, mock_get_classifiers):
        """Test that _classify returns None when there are no classifiers."""
        mock_get_classifiers.return_value = []

        mock_token = Mock()
        mock_token.string = 'some_token'

        checker = Checker(ast.parse(''), [])

        result = checker._classify(mock_token)

        assert result is None

    def test_classify_returns_number_when_classifier_finds_match(self):
        """Test that _classify returns the number when a classifier finds a match."""
        mock_token = Mock()
        mock_token.string = '123'  # Regular integer that IntClassifier will handle

        checker = Checker(ast.parse(''), [])

        result = checker._classify(mock_token)

        assert result is not None
        assert hasattr(result, 'token')
        assert result.token == '123'

    @patch('flake8_digit_separator.checker.Checker._classify')
    def test_process_number_token_returns_none_when_classify_returns_none(self, mock_classify):
        """Test that _process_number_token returns None when _classify returns None."""
        mock_classify.return_value = None

        mock_token = Mock()
        mock_token.string = 'some_token'

        checker = Checker(ast.parse(''), [])

        result = checker._process_number_token(mock_token)

        assert result is None

    def test_process_number_token_returns_none_for_unsupported_number(self):
        """Test that _process_number_token returns None for unsupported numbers."""
        mock_token = Mock()
        mock_token.string = '1e10'  # Scientific notation (unsupported)

        checker = Checker(ast.parse(''), [])

        result = checker._process_number_token(mock_token)

        assert result is None

    def test_run_yields_errors_for_invalid_numbers(self):
        """Test that run() method yields errors for invalid numbers."""
        mock_token = Mock()
        mock_token.type = 2  # tokenize.NUMBER
        mock_token.string = '1234'  # Invalid int (no separators)
        mock_token.start = (1, 0)  # Line 1, column 0

        checker = Checker(ast.parse(''), [mock_token])

        errors = list(checker.run())

        assert len(errors) == 1
        assert errors[0][0] == 1  # Line number
        assert errors[0][1] == 0  # Column number
        assert 'FDS100' in errors[0][2]  # Error message

    def test_run_skips_non_number_tokens(self):
        """Test that run() method skips non-number tokens."""
        mock_token = Mock()
        mock_token.type = 1  # tokenize.NAME (not NUMBER)
        mock_token.string = 'variable_name'

        checker = Checker(ast.parse(''), [mock_token])

        errors = list(checker.run())

        assert len(errors) == 0

    @patch('flake8_digit_separator.checker.ValidatorRegistry.get_validator')
    @patch('flake8_digit_separator.checker.Checker._classify')
    def test_process_number_token_returns_error_when_validation_fails(self, mock_classify, mock_get_validator):
        """Test that _process_number_token returns error when validation fails."""
        mock_number = Mock()
        mock_number.is_supported = True
        mock_number.token = '1234'  # Add token attribute for _should_exclude_number
        mock_classify.return_value = mock_number

        mock_validator = Mock()
        mock_validator.validate.return_value = False
        mock_validator.error_message = 'FDS100: Test error message'
        mock_get_validator.return_value = mock_validator

        mock_token = Mock()
        mock_token.string = '1234'
        mock_token.start = (1, 0)

        checker = Checker(ast.parse(''), [])

        result = checker._process_number_token(mock_token)

        assert result is not None
        assert result.line == 1
        assert result.column == 0
        assert result.message == 'FDS100: Test error message'

    @patch('flake8_digit_separator.checker.ValidatorRegistry.get_validator')
    @patch('flake8_digit_separator.checker.Checker._classify')
    def test_process_number_token_returns_none_when_validation_passes(self, mock_classify, mock_get_validator):
        """Test that _process_number_token returns None when validation passes."""
        mock_number = Mock()
        mock_number.is_supported = True
        mock_number.token = '1234'  # Add token attribute for _should_exclude_number
        mock_classify.return_value = mock_number

        mock_validator = Mock()
        mock_validator.validate.return_value = True
        mock_get_validator.return_value = mock_validator

        mock_token = Mock()
        mock_token.string = '1234'
        mock_token.start = (1, 0)

        checker = Checker(ast.parse(''), [])

        result = checker._process_number_token(mock_token)

        assert result is None
