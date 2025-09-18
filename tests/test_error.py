from flake8_digit_separator.error import Error


class TestError:
    """Test Error class."""

    def test_as_tuple_returns_correct_tuple(self):
        """Test that as_tuple() returns the correct tuple format."""
        error = Error(
            line=10,
            column=5,
            message='FDS100: Test error message',
            object_type=type(self),
        )

        result = error.as_tuple()
        args_count = 4

        assert result == (10, 5, 'FDS100: Test error message', type(self))
        assert isinstance(result, tuple)
        assert len(result) == args_count
