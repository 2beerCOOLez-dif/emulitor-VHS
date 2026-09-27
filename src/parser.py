"""Модуль для разбора пользовательского ввода на команды и аргументы""" 

def parse_input(user_input: str) -> tuple[str, list[str]]: 
    """эта функция парсит команду пользователя и разделяет её по пробелам""" 

    parts = user_input.strip().split()
    if not parts:
        return "", []

    return parts[0], parts[1:]
