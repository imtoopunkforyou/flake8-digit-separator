import subprocess
from pathlib import Path

import pytest

from tests.e2e.cases import wrong


@pytest.fixture
def path_to_wrong_cases():
    base_dir = Path(__file__).parent
    return base_dir / 'cases' / 'wrong.py'


@pytest.fixture
def path_to_correct_cases():
    base_dir = Path(__file__).parent
    return base_dir / 'cases' / 'correct.py'


@pytest.fixture
def fds100_wrong_count():
    return len(wrong.FDS100)


@pytest.fixture
def fds200_wrong_count():
    return len(wrong.FDS200)


@pytest.fixture
def fds300_wrong_count():
    return len(wrong.FDS300)


@pytest.fixture
def fds400_wrong_count():
    return len(wrong.FDS400)


@pytest.fixture
def fds500_wrong_count():
    return len(wrong.FDS500)


@pytest.fixture
def flake8_stdout():
    def _flake8_stdout(file_path):
        process = subprocess.Popen(
            (
                'flake8',
                '--isolated',
                '--show-source',
                '--select',
                'FDS',
                file_path,
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = process.communicate()
        return stdout

    return _flake8_stdout
