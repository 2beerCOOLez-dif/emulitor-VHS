"""Модул для REPL"""
from src.parser import parse_input
from src.commands import execute_ls, execute_cd

VFS_NAME = "Stariy"

def run_repl() -> None:
    """Запуск интервального цикла REPL"""
    print(f"Welcome to {VFS_NAME} emulator!")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input(f"{VFS_NAME}> ")

        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        command, args = parse_input(user_input)

        if not command:
            continue

        if command == "exit":
            print("Goodbye!")
            break
        elif command == "ls":
            print(execute_ls(args))
        elif command == "cd":
            print(execute_cd(args))
        else:
            print(f"Error: unknown command '{command}'")