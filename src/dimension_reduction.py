from sklearn.decomposition import PCA

# Функция снижения размерности эмбеддингов

def reducing_dimension_of_embeddings(embeddings):

    pca = PCA(n_components=2) # Уменьшаем до 2D размерности
    embeddings_reduced = pca.fit_transform(embeddings)

    return(embeddings_reduced)