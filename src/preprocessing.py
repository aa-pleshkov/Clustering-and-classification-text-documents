# src/preprocessing.py
import os
import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from config import PROCESSED_DATA_DIR

# Загружаем ресурсы для предварительной обработки текстовых файлов

#nltk.download('punkt')  # Загрузка необходимых ресурсов для токенизации

nltk.download('stopwords') # Загрузка необходимых ресурсов для удаления стоп-слов
stop_words = set(stopwords.words('english'))

nlp = spacy.load("en_core_web_sm") # Загрузка языковой модели библиотеки spacy для лемматизации текста



# Функция для считывания всех текстовых файлов из исходной папки:

def read_downloaded_text_files(data_dir):
    texts = []  # Список для хранения текстов
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                texts.append(content)  # Добавляем текст в список
    return texts



# Функция для предварительной обработки каждого текстового файла:

def pre_processing_text_files(texts):
    temporary_list = []
    
    for text in texts:
        # 1. Приведение текста к нижнему регистру
        text = text.lower()

        # 2. Регулярное выражение для удаления знаков препинания, табуляции и переносов строк
        text = re.sub(r'[^\w\s]|[\t\n]', '', text)

        # 3. Токенизация
        tokens = word_tokenize(text)
        temporary_list.append(tokens)

    # 4. Удаление стоп слов и лемматизация
    processed_text = [[nlp(word)[0].lemma_ for word in temporary_list[i] if word not in stop_words] for i in range(len(temporary_list))]

    temporary_list.clear()

    return(processed_text)


# Функция, которая сохраняет предобработанные текстовые файлы в файл processed.txt в папке data:

def save_results_of_pre_processed_text_files_in_data_foulder(processed_text):
    with open(PROCESSED_DATA_DIR, 'w', encoding='utf-8') as f:
        for elem in processed_text:
            full_pre_processed_text_file = ' '.join(elem[i] for i in range(len(elem)))
            f.write(f'{processed_text.index(elem) + 1} pre processed file: ' + full_pre_processed_text_file)
            f.write('\n')
