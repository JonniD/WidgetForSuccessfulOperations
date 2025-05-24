from functools import wraps
from typing import Any, Callable, Literal


def log(filename: Literal[False] | str = False) -> Callable[[Any], Any]:
    """Функция-декоратор для ведения логов.
    Записывает лог в файл, если задано имя файла, и в консоль - если нет."""

    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator
