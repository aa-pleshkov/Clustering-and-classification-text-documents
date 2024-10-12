# scripts/main.py
from preprocessing import read_downloaded_text_files, pre_processing_text_files
from preprocessing import save_results_of_pre_processed_text_files_in_data_foulder
from embeddings import get_embeddings_from_pre_processed_text_files, save_embeddings
from clustering import usе_elbow_method_to_find_optimal_number_of_clusters
from clustering import clustering_of_embeddings_obtained_from_processed_text_files
from clustering import save_cluster_centers_and_labels, load_cluster_centers_and_labels
from predict import predict_the_nearest_cluster_for_new_text_file
from add_new_text_file import check_the_existence_of_new_text_file
from config import DATA_DIR

if __name__ == '__main__':

    # Считываем текстовые файлы
    text_files = read_downloaded_text_files(DATA_DIR)
    
    # Обрабатываем тексты
    processed_text_files = pre_processing_text_files(text_files)

    # Сохраняем результы предварительной обработки текстовых файлов в файл - processed.txt папки data
    #save_results_of_pre_processed_text_files_in_data_foulder(processed_text_files)

    # Переход к векторному представлению (создание эмбеддингов предобработанных текстовых документов)
    result_embeddings = get_embeddings_from_pre_processed_text_files(processed_text_files)

    # Сохраняем эмбеддинги в файл embeddings.npy папки data
    #save_embeddings(result_embeddings, EMBEDDINGS_DATA_DIR)

    # Нахождение оптимального количества кластеров с помощью метода локтя
    optimal_k = usе_elbow_method_to_find_optimal_number_of_clusters(result_embeddings)

    # Кластеризация эмбеддингов, функция возвращает центры кластеров и массив labels(который содержит распределение эмбеддингов по кластерам)
    labels, cluster_centers = clustering_of_embeddings_obtained_from_processed_text_files(result_embeddings, optimal_k)

    # Сохранение значений центров кластеров в файл cluster_centers.pkl(data), сохранение значений labels в labels.pkl(data)
    save_cluster_centers_and_labels(cluster_centers, labels)

    loaded_clusters, loaded_labels = load_cluster_centers_and_labels()
    print(loaded_labels)

    # Проверка наличия нового текстового файла для нахождения ближайшего кластера
    new_text_file = check_the_existence_of_new_text_file()

    if new_text_file:

        nearest_cluster = predict_the_nearest_cluster_for_new_text_file(new_text_file, cluster_centers)

        print(f'Ближайший кластер для нового текстового файла: {nearest_cluster}')