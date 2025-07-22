import ast
import tokenize
from unittest.mock import Mock, patch

import pytest

from flake8_digit_separator.checker import Checker


class TestChecker:
    """Test Checker class."""

    @patch('flake8_digit_separator.checker.ClassifierRegistry.get_ordered_classifiers')
    def test_classify_returns_none_when_all_classifiers_return_none(self, mock_get_classifiers):
        """Test that _classify returns None when all classifiers return None."""
        # Mock classifiers that all return None
        mock_classifier_cls = Mock()
        mock_classifier_instance = Mock()
        mock_classifier_instance.classify.return_value = None
        mock_classifier_cls.return_value = mock_classifier_instance
        
        mock_get_classifiers.return_value = [mock_classifier_cls]
        
        # Create a mock token
        mock_token = Mock()
        mock_token.string = "some_token"
        
        # Create checker instance
        checker = Checker(ast.parse(""), [])
        
        # Call _classify method
        result = checker._classify(mock_token)
        
        # Should return None when all classifiers return None
        assert result is None

    @patch('flake8_digit_separator.checker.ClassifierRegistry.get_ordered_classifiers')
    def test_classify_returns_none_when_all_classifiers_return_falsy(self, mock_get_classifiers):
        """Test that _classify returns None when all classifiers return falsy values."""
        # Mock multiple classifiers that return various falsy values
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
        
        # Create a mock token
        mock_token = Mock()
        mock_token.string = "some_token"
        
        # Create checker instance
        checker = Checker(ast.parse(""), [])
        
        # Call _classify method
        result = checker._classify(mock_token)
        
        # Should return None when all classifiers return falsy values
        assert result is None

    @patch('flake8_digit_separator.checker.ClassifierRegistry.get_ordered_classifiers')
    def test_classify_returns_none_when_no_classifiers(self, mock_get_classifiers):
        """Test that _classify returns None when there are no classifiers."""
        # Mock empty list of classifiers
        mock_get_classifiers.return_value = []
        
        # Create a mock token
        mock_token = Mock()
        mock_token.string = "some_token"
        
        # Create checker instance
        checker = Checker(ast.parse(""), [])
        
        # Call _classify method
        result = checker._classify(mock_token)
        
        # Should return None when there are no classifiers
        assert result is None

    def test_classify_returns_number_when_classifier_finds_match(self):
        """Test that _classify returns the number when a classifier finds a match."""
        # Create a mock token
        mock_token = Mock()
        mock_token.string = "123"  # Regular integer that IntClassifier will handle
        
        # Create checker instance
        checker = Checker(ast.parse(""), [])
        
        # Call _classify method
        result = checker._classify(mock_token)
        
        # Should return the classified number (not None)
        assert result is not None
        assert hasattr(result, 'token')
        assert result.token == "123"

    @patch('flake8_digit_separator.checker.Checker._classify')
    def test_process_number_token_returns_none_when_classify_returns_none(self, mock_classify):
        """Test that _process_number_token returns None when _classify returns None."""
        # Mock _classify to return None
        mock_classify.return_value = None
        
        # Create a mock token
        mock_token = Mock()
        mock_token.string = "some_token"
        
        # Create checker instance
        checker = Checker(ast.parse(""), [])
        
        # Call _process_number_token method
        result = checker._process_number_token(mock_token)
        
        # Should return None when _classify returns None
        assert result is None

    def test_process_number_token_returns_none_for_unsupported_number(self):
        """Test that _process_number_token returns None for unsupported numbers."""
        # Create a mock token
        mock_token = Mock()
        mock_token.string = "1e10"  # Scientific notation (unsupported)
        
        # Create checker instance
        checker = Checker(ast.parse(""), [])
        
        # Call _process_number_token method - scientific numbers are unsupported
        result = checker._process_number_token(mock_token)
        
        # Should return None because scientific numbers have is_supported=False
        assert result is None 