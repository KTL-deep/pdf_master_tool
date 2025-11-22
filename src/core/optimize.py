import os
from typing import List, Union
from pypdf import PdfReader, PdfWriter


class PDFOrganizer:
    """
    Модуль для организации страниц PDF:
    - Объединение (Merge)
    - Разделение (Split)
    - Удаление/Перестановка страниц
    - Извлечение изображений
    """

    def merge_pdfs(self, file_paths: List[str], output_path: str) -> bool:
        """
        Объединяет несколько PDF файлов в один.
        :param file_paths: Список путей к файлам ['1.pdf', '2.pdf']
        :param output_path: Путь сохранения результата
        """
        try:
            writer = PdfWriter()

            for path in file_paths:
                reader = PdfReader(path)
                for page in reader.pages:
                    writer.add_page(page)

            with open(output_path, "wb") as f_out:
                writer.write(f_out)

            print(f"[OK] Файлы успешно объединены в: {output_path}")
            return True
        except Exception as e:
            print(f"[ERROR] Ошибка при объединении: {e}")
            return False

    def split_pdf(self, file_path: str, output_folder: str) -> bool:
        """
        Разделяет PDF на отдельные страницы.
        Сохраняет как page_1.pdf, page_2.pdf и т.д.
        """
        try:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            reader = PdfReader(file_path)

            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)

                output_filename = os.path.join(output_folder, f"page_{i + 1}.pdf")
                with open(output_filename, "wb") as f_out:
                    writer.write(f_out)

            print(f"[OK] Файл разделен на {len(reader.pages)} страниц в папке: {output_folder}")
            return True
        except Exception as e:
            print(f"[ERROR] Ошибка при разделении: {e}")
            return False

    def reorder_or_delete_pages(self, file_path: str, output_path: str, page_indices: List[int]) -> bool:
        """
        Создает новый PDF, оставляя только указанные страницы в заданном порядке.
        Используется для:
        - Удаления страниц (просто не включайте их индекс в список)
        - Изменения порядка (передайте индексы в новом порядке)
        :param page_indices: Список номеров страниц (начиная с 0). Пример: [0, 2, 5]
        """
        try:
            reader = PdfReader(file_path)
            writer = PdfWriter()

            total_pages = len(reader.pages)

            for index in page_indices:
                if 0 <= index < total_pages:
                    writer.add_page(reader.pages[index])
                else:
                    print(f"[WARNING] Страница {index} пропущена (вне диапазона)")

            with open(output_path, "wb") as f_out:
                writer.write(f_out)

            print(f"[OK] Новый файл сохранен: {output_path}")
            return True
        except Exception as e:
            print(f"[ERROR] Ошибка при пересортировке: {e}")
            return False

    def extract_images(self, file_path: str, output_folder: str) -> int:
        """
        Извлекает встроенные изображения из PDF.
        Возвращает количество извлеченных изображений.
        """
        try:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            reader = PdfReader(file_path)
            count = 0

            for page_num, page in enumerate(reader.pages):
                for img_file_obj in page.images:
                    with open(os.path.join(output_folder, f"p{page_num}_{img_file_obj.name}"), "wb") as fp:
                        fp.write(img_file_obj.data)
                    count += 1

            print(f"[OK] Извлечено {count} изображений в: {output_folder}")
            return count
        except Exception as e:
            print(f"[ERROR] Ошибка при извлечении изображений: {e}")
            return 0