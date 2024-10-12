import pandas as pd
import numpy as np
import sentence_transformers
from sentence_transformers import SentenceTransformer

# Загружаем предобученную модель
model = SentenceTransformer('all-MiniLM-L6-v2')

# Функция для получение эмбеддингов из обработанных текстовых файлов
def get_embeddings_from_pre_processed_text_files(text_lists):
    embeddings = []
    for word_list in text_lists:
        # Соединяем слова в строку
        text = ' '.join(word_list)
        # Получаем эмбеддинг
        embedding = model.encode(text)
        embeddings.append(embedding)
    
    return embeddings

# Функция для сохранения эмбеддингов в файл - embeddings.npy папки data
def save_embeddings(embeddings, file_path):
    np.save(file_path, embeddings)
