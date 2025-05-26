def test_wrong_fds100(path_to_wrong_cases, flake8_stdout, fds100_wrong_count):
    stdout = flake8_stdout(path_to_wrong_cases)

    assert stdout.count(b'FDS100') == fds100_wrong_count


# def test_wrong_fds200(path_to_wrong_cases, flake8_stdout, fds200_wrong_count):
#     stdout = flake8_stdout(path_to_wrong_cases)

#     assert stdout.count(b'FDS200') == fds200_wrong_count


# def test_wrong_fds300(path_to_wrong_cases, flake8_stdout, fds300_wrong_count):
#     stdout = flake8_stdout(path_to_wrong_cases)

#     assert stdout.count(b'FDS300') == fds300_wrong_count


# def test_wrong_fds400(path_to_wrong_cases, flake8_stdout, fds400_wrong_count):
#     stdout = flake8_stdout(path_to_wrong_cases)

#     assert stdout.count(b'FDS400') == fds400_wrong_count


# def test_wrong_fds500(path_to_wrong_cases, flake8_stdout, fds500_wrong_count):
#     stdout = flake8_stdout(path_to_wrong_cases)

#     assert stdout.count(b'FDS500') == fds500_wrong_count
