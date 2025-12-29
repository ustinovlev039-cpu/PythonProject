from functools import wraps
from typing import Any
from typing import Callable
from typing import Optional


def log(func: Optional[Callable : [str | int]] = None, *, filename: Optional[str] = None) -> Any:
    """Декоратор логирует начало/конец выполнения функции, результат или ошибку.
    Если filename задан — пишет в файл, иначе печатает в консоль."""
    if func is None:

        def decorator(real_func):
            return log(real_func, filename=filename)

        return decorator

    def write(message: str):
        if filename is None:
            print(message)
        else:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(message + "\n")

    @wraps(func)
    def wrapper(*args, **kwargs):
        write(f"START {func.__name__} args={args} kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            write(f"ERROR {func.__name__} {type(e).__name__} args={args} kwargs={kwargs}")
            raise
        else:
            write(f"END {func.__name__} result={result}")
            return result

    return wrapper
