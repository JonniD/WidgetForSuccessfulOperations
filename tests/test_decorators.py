import pytest
from src.decorators import log
import tempfile
import os


def test_log_success(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n'


def test_log_to_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    @log(filename=filename)
    def test_func(x):
        return x

    test_func(1)

    with open(filename) as f:
        content = f.read()

    os.unlink(filename)
    assert "test_func ok" in content


def test_log_error(capsys):
    @log()
    def test_func(a, b):
        raise ValueError('test error')

    try:
        test_func(1, 2)
    except ValueError:
        pass

    captured = capsys.readouterr()
    assert 'test_func error: ValueError. Inputs: (1, 2), {}\n' in captured.out

def test_log_error_file(capsys):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name
    @log(filename=filename)
    def test_func(a, b):
        raise ValueError('test error')

    try:
        test_func(1, 2)
    except ValueError:
        pass

    with open(filename) as f:
        content = f.read()

    os.unlink(filename)
    assert 'test_func error: ValueError. Inputs: (1, 2), {}\n' in content