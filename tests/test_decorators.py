
import pytest
from src.decorators import log

def test_console_success(capsys):
    @log
    def add(a, b):
        return a + b

    assert add(2, 5) == 7

    captured = capsys.readouterr().out
    assert "START add" in captured
    assert "END add" in captured
    assert "result=7" in captured



def test_console_error(capsys):
    @log
    def boom(x):
        raise ValueError("bad")

    with pytest.raises(ValueError):
        boom(10)

    captured = capsys.readouterr().out
    assert "START boom" in captured
    assert "ERROR boom ValueError" in captured
    assert "args=(10,)" in captured

def test_file_success(tmp_path):
    log_file = tmp_path / "app.log"

    @log(filename=str(log_file))
    def mul(a, b):
        return a * b

    assert mul(4, 5) == 20

    text = log_file.read_text(encoding="utf-8")
    assert "START mul" in text
    assert "END mul" in text
    assert "result=20" in text


def test_file_error(tmp_path):
    log_file = tmp_path / "errors.log"

    @log(filename=str(log_file))
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    text = log_file.read_text(encoding="utf-8")
    assert "START div" in text
    assert "ERROR div ZeroDivisionError" in text
    assert "args=(1, 0)" in text

def test_log_with_parentheses_works(capsys):
    @log()
    def f():
        return "ok"

    assert f() == "ok"
    captured = capsys.readouterr().out
    assert "START f" in captured
    assert "END f" in captured
    assert "result=ok" in captured






