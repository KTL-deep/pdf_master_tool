import sys
import os

# Добавляем путь к src, чтобы Python видел наши модули
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.core import organize, optimize


def main():
    print("=== PDF Master Tool Запущен ===")
    print(f"Версия Python: {sys.version}")
    print("Структура проекта успешно инициализирована.")

    # Пример проверки импорта модулей
    if organize and optimize:
        print("Модули ядра (Core) подключены корректно.")


if __name__ == "__main__":
    main()
