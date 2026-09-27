"""Тесты для модуля парсера"""
from src.parser import parse_input


def test_parse_empty_input():
    """тесты с пустой строкой"""
    assert parse_input("") == ("", [])
    assert parse_input("   ") == ("", [])


def test_parse_single_command():
    """Тесты для строки без аргемунтов"""
    assert parse_input("ls") == ("ls", [])


def test_parse_command_with_args():
    """Тесты для нескольких аргументов"""
    assert parse_input("cd folder") == ("cd", ["folder"])
    assert parse_input("ls -l -a") == ("ls", ["-l", "-a"])


def test_parse_command_with_extra_spaces():
    """Тесты на обрабатывание нескольких пробелов"""
    assert parse_input("  ls   folder  ") == ("ls", ["folder"])