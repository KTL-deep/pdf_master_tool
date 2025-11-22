import os
from src.core.organize import PDFOrganizer


def test_organize():
    # Настройка путей (замените 'test.pdf' на имя вашего файла в папке data)
    source_pdf = os.path.join("data", "test.pdf")
    output_folder = os.path.join("data", "output_test")

    # Создаем экземпляр нашего класса
    organizer = PDFOrganizer()

    # Проверка 1: Разделение файла
    print("--- Тест 1: Разделение PDF ---")
    if os.path.exists(source_pdf):
        organizer.split_pdf(source_pdf, output_folder)
    else:
        print(f"Файл {source_pdf} не найден! Положите любой PDF в папку data.")


if __name__ == "__main__":
    test_organize()