"""Тесты для модуля парсера"""
from src.parser import parse_input

def test_parse_empty_input():
    """тест пустой строки"""
    assert parse_input("") == ("", [])
    assert parse_input("   ") == ("", [])

def test_parse_single_command():
    """тест одной команды ьез аргументов"""
    assert parse_input("ls") == ("ls", [])

def test_parse_command_with_args():
    """тест с несколькими аргументами"""
    assert parse_input("cd folder") == ("cd", ["folder"])
    assert parse_input("ls -l -a") == ("ls", ["-l", "-a"])