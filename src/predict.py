from preprocessing import pre_processing_text_files
from embeddings import get_embeddings_from_pre_processed_text_files
from dimension_reduction import reducing_dimension_of_embeddings
from sklearn.metrics.pairwise import cosine_distances
import numpy as np

def predict_the_nearest_cluster_for_new_text_file(new_text_file, cluster_centers):

    processed_new_text_file = pre_processing_text_files(new_text_file)

    embedding_for_new_text_file = get_embeddings_from_pre_processed_text_files(processed_new_text_file)

    reduce_embedding_for_new_text_file = reducing_dimension_of_embeddings(embedding_for_new_text_file)

    reduce_cluster_centers = reducing_dimension_of_embeddings(cluster_centers)

    distances = cosine_distances(reduce_embedding_for_new_text_file, reduce_cluster_centers)[0]

    min_index = np.argmin(distances)
    
    return(min_index)