import os
from config import NEW_TEXT_FILE_DATA_DIR

def check_the_existence_of_new_text_file():

    # Получение списка файлов в директории
    files = os.listdir(NEW_TEXT_FILE_DATA_DIR)

    # Проверка наличия текстовых файлов
    if files:
        text_files = [file for file in files if file.endswith('.txt')]
        # Если текстовые файлы найдены, открываем и читаем первый из них
        txt_file_path = os.path.join(NEW_TEXT_FILE_DATA_DIR, text_files[0])  # Путь к первому текстовому файлу

        # Открытие и чтение файла
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Сохраняем содержимое в список content
            return content
    else:
        print('Текстовый файл еще не добавлен в папку new_text_file')