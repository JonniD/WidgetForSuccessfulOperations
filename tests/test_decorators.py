import os
import tempfile
from typing import Any

from src.decorators import log


def test_log_success(capsys: Any) -> None:
    """тест функции - декоратора log с функцией которая не вызывает ошибку и не задан файл для записи лога"""

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_to_file() -> None:
    """тест функции - декоратора log с функцией которая не вызывает ошибку и задан файл для записи лога"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    @log(filename=filename)
    def test_func(x: int) -> int:
        return x

    test_func(1)

    with open(filename) as f:
        content = f.read()

    os.unlink(filename)
    assert "test_func ok" in content


def test_log_error(capsys: Any) -> None:
    """тест функции - декоратора log с функцией которая вызывает ошибку и не задан файл для записи лога"""

    @log()
    def test_func(a: int, b: int) -> None:
        raise ValueError("test error")

    try:
        test_func(1, 2)
    except ValueError:
        pass

    captured = capsys.readouterr()
    assert "test_func error: ValueError. Inputs: (1, 2), {}\n" in captured.out


def test_log_error_file(capsys: Any) -> None:
    """тест функции - декоратора log с функцией которая вызывает ошибку и задан файл для записи лога"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    @log(filename=filename)
    def test_func(a: int, b: int) -> None:
        raise ValueError("test error")

    try:
        test_func(1, 2)
    except ValueError:
        pass

    with open(filename) as f:
        content = f.read()

    os.unlink(filename)
    assert "test_func error: ValueError. Inputs: (1, 2), {}\n" in content
