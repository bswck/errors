import pytest

from errors._compat import BaseExceptionGroup, ExceptionGroup


# YORE: EOL 3.9: 🔪
@pytest.mark.skipif("sys.version_info < (3, 11)")
def test_correct_group_classes() -> None:
    assert not BaseExceptionGroup.__module__.startswith("exceptiongroup")
    assert not ExceptionGroup.__module__.startswith("exceptiongroup")
