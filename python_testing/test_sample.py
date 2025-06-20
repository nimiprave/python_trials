from addFunction import add
import pytest


def func(x):
    return x + 1


def exceptionGroupFunction():
    raise ExceptionGroup(
        "Group message", [RuntimeError()])


def exceptionFunction():
    raise SystemExit(1)


def test_answer():
    assert func(3) == 4


def test_add():
    assert add(1, 2) == 3


def test_exception():
    with pytest.raises(SystemExit):
        exceptionFunction()


def test_group_exception():
    with pytest.raises(ExceptionGroup) as excinfo:
        exceptionGroupFunction()
        assert excinfo.group_contains(RuntimeError)
        assert not excinfo.group_contains(TypeError)
