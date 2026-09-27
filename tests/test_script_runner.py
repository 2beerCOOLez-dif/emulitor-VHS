"""Тест для script_runner"""
from pathlib import Path
import pytest
from src.script_runner import run_script


def _write_script(tmp_path: Path, content: str) -> Path:
    """Помощник для создания временного файла скрипта.

    Аргументы:
        tmp_path: временный каталог Pytest.
        содержимое: содержимое скрипта для записи.

    Возвращается:
        Путь к созданному файлу скрипта.
    """
    script = tmp_path / "test.sh"
    script.write_text(content, encoding="utf-8")
    return script


def test_run_script_with_comments(capsys, tmp_path):
    """Проверка, что комментарии пропускались во время выполнения"""
    script = _write_script(tmp_path, "# comment\nls\n")
    run_script(script)
    captured = capsys.readouterr()
    assert "ls called" in captured.out
    assert "# THIS_IS_COMMENT" not in captured.out


def test_run_script_with_exit(capsys, tmp_path):
    """Проверка, что команда exit останавливает выполнение скрипта"""
    content = "ls\nexit\nls\n"
    script = _write_script(tmp_path, content)
    run_script(script)
    captured = capsys.readouterr()
    assert captured.out.count("ls called") == 1


def test_run_script_file_not_found():
    """Проверка, что команда exit останавливает выполнение скрипта"""
    with pytest.raises(FileNotFoundError):
        run_script(Path("nonexistent.sh"))


def test_run_script_empty_file(capsys, tmp_path):
    """Проверка, работает ли пустой скрипт без ошибок."""
    script = _write_script(tmp_path, "")
    run_script(script)
    captured = capsys.readouterr()
    assert "Script finished" in captured.out