def test_correct(path_to_correct_cases, flake8_stdout):
    stdout = flake8_stdout(path_to_correct_cases)

    assert stdout.count(b'FDS100') == 0
    assert stdout.count(b'FDS200') == 0
    # assert stdout.count(b'FDS300') == 0
    # assert stdout.count(b'FDS400') == 0
    # assert stdout.count(b'FDS500') == 0
