import numpy as np
import matplotlib
import sklearn
import pickle
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from config import CLUSTER_CENTERS_DATA_DIR
from config import LABELS_DATA_DIR

# Выбор оптимального количества кластеров с помощью метода локтя

def usе_elbow_method_to_find_optimal_number_of_clusters(embeddings, max_k=3):

    wcss = []  # Список для хранения WCSS
    
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(embeddings)
        wcss.append(kmeans.inertia_)  # Добавляем WCSS в список
    
    optimal_k = np.diff(wcss, 2).argmin() + 2  # +2, чтобы учесть смещение из-за diff
    #print(f"Оптимальное количество кластеров: {optimal_k}")

    wcss.clear()
    
    return optimal_k



# Кластеризация с использованием KMeans

def clustering_of_embeddings_obtained_from_processed_text_files(embeddings, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    cluster_centers = kmeans.cluster_centers_

    return labels, cluster_centers



# Функция для сохранения центров кластеров и меток

def save_cluster_centers_and_labels(cluster_centers, labels_data):
    
    with open(CLUSTER_CENTERS_DATA_DIR, 'wb') as cluster_centers_file:
        pickle.dump(cluster_centers, cluster_centers_file)
    
    with open(LABELS_DATA_DIR, 'wb') as labels_file:
        pickle.dump(labels_data, labels_file)

def load_cluster_centers_and_labels():
    
    with open(CLUSTER_CENTERS_DATA_DIR, 'rb') as cluster_centers_file:
        loaded_cluster_centers = pickle.load(cluster_centers_file)
    
    with open(LABELS_DATA_DIR, 'rb') as labels_file:
        loaded_labels = pickle.load(labels_file)
    
    return loaded_cluster_centers, loaded_labels