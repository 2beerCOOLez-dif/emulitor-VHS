"""Главная точка входа эмулятора VFS"""

import sys
from src.config import parse_args
from src.repl import run_repl
from src.script_runner import run_script


def main() -> None:
    """Выполняет основную логику приложения"""
    config = parse_args()

    print("VFS Shell Emulator")
    print(f"VFS path: {config.vfs_path}")
    print(f"Script path: {config.script_path}")

    if config.script_path is not None:
        try:
            run_script(config.script_path)
        except FileNotFoundError as error:
            print(f"Error: {error}", file=sys.stderr)
            sys.exit(1)

        return

    run_repl()

if __name__ == "__main__":
    main()