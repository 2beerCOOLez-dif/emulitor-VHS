"""Модуль для обработки аргументов командной строки и настройки"""

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppConfig:
    """Сохраняет все параметры конфигурации для эмулятора.
    Атрибуты:
        vfs_path: Путь к файлу виртуальной файловой системы.
        script_path: путь к файлу сценария запуска.
    """

    vfs_path: Path | None
    script_path: Path | None


def parse_args() -> AppConfig:
    """Проанализирует аргументы командной строки и вернёт конфигурацию.

    Возвращается:
        Экземпляр AppConfig с проанализированными параметрами.
    """

    parser = argparse.ArgumentParser(
        description="VFS Shell Emulator"
    )

    parser.add_argument(
        "--vfs-path",
        type=Path,
        default=None,
        help="Path to the virtual file system file",
    )

    parser.add_argument(
        "--script",
        type=Path,
        default=None,
        help="Path to the startup script file",
    )

    args = parser.parse_args()

    # Создаём новую "коробку" AppConfig и кладём в неё значения из args
    # Возвращаем эту коробку тому, кто вызвал функцию
    return AppConfig(
        vfs_path=args.vfs_path,
        script_path=args.script,
    )