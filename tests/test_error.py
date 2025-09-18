from flake8_digit_separator.error import Error


def test_error_as_tuple_returns_correct_tuple():
    """Test that as_tuple() returns the correct tuple format."""
    error = Error(
        line=10,
        column=5,
        message='FDS100: Test error message',
        object_type=type(test_error_as_tuple_returns_correct_tuple),
    )

    result = error.as_tuple()
    args_count = 4

    assert result == (10, 5, 'FDS100: Test error message', type(test_error_as_tuple_returns_correct_tuple))
    assert isinstance(result, tuple)
    assert len(result) == args_count
