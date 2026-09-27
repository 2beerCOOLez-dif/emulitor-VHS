"""Модуль, который содержит заглушки команд и логику"""

def execute_ls(args: list[str]) -> str:
    """выполнение заглушку команды ls"""
    # Если аргументы есть, соединяем их через запятую. Если нет, пишем "none"
    args_str = ", ".join(args) if args else "none"
    return f"ls called with args: {args_str}" # Возвращаем красивую строку

def execute_cd(args: list[str]) -> str:
    """выполнение заглушку команды cd"""
    args_str = ", ".join(args) if args else "none"
    return f"cd called with args: {args_str}"