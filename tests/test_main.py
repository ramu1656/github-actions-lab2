import sys
import pathlib

# Ensure the repository root is on sys.path so tests can import `main` even
# when pytest is invoked from the `tests` directory or by other tools that
# change the CWD. This is a small, safe shim that's commonly used in tests.
repo_root = pathlib.Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

import pytest
from main import sum_two_integers


def test_sum_two_integers_positive():
    assert sum_two_integers(3, 5) == 8
