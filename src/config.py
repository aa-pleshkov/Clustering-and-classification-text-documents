# src/config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Получаем путь к текущей директории
DATA_DIR = os.path.join(BASE_DIR, '../initial_data_set')  # Создаем путь к папке с текстами
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, '../data/processed.txt')  # Папка для хранения обработанных текстов
EMBEDDINGS_DATA_DIR = os.path.join(BASE_DIR, '../data/embeddings.npy') # Файл для хранения эмбеддингов
CLUSTER_CENTERS_DATA_DIR = os.path.join(BASE_DIR, '../data/cluster_centers.pkl') # Файл для хранения центров кластеров
LABELS_DATA_DIR = os.path.join(BASE_DIR, '../data/labels.pkl') # Файл для хранения списка labels
NEW_TEXT_FILE_DATA_DIR = os.path.join(BASE_DIR, '../new_text_file') # Файл для хранения нового текстового файла