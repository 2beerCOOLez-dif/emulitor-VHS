"""Модуль для выполнения сценариев запуска"""

from pathlib import Path
from src.parser import parse_input
from src.commands import execute_ls, execute_cd


COMMENT_PREFIX = "#"


def run_script(script_path: Path) -> None:
    """Выполняет команды из файла сценария запуска.

    Каждая строка рассматривается как команда. Строки, начинающиеся с "#"
    рассматриваются как комментарии и пропускаются.

    Аргументы:
        script_path: Путь к файлу сценария для выполнения.

    Повышения:
        FileNotFoundError: Если файл скрипта не существует.
    """

    if not script_path.exists():
        raise FileNotFoundError(
            f"Script file not found: {script_path}"
        )

    print(f"--- Running script: {script_path} ---")

    with open(script_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(COMMENT_PREFIX):
                continue

            print(f"my_vfs> {line}")

            command, args = parse_input(line)

            if command == "exit":
                print("Goodbye!")
                break
            elif command == "ls":
                print(execute_ls(args))
            elif command == "cd":
                print(execute_cd(args))
            else:
                print(f"Error: unknown command '{command}'")

    print("--- Script finished ---")