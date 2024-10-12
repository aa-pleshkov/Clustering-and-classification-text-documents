import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Генерация случайных эмбеддингов
np.random.seed(42)  # Для воспроизводимости
n_samples = 100
n_features = 3
n_clusters = 4

# Создаем случайные эмбеддинги
embeddings = np.random.rand(n_samples, n_features)

# Кластеризация с помощью KMeans
kmeans = KMeans(n_clusters=n_clusters)
labels = kmeans.fit_predict(embeddings)
centers = kmeans.cluster_centers_

# Визуализация результатов
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Цвета для кластеров
colors = plt.cm.jet(np.linspace(0, 1, n_clusters))

# Отображение эмбеддингов
for i in range(n_clusters):
    ax.scatter(embeddings[labels == i, 0],
               embeddings[labels == i, 1],
               embeddings[labels == i, 2],
               color=colors[i], label=f'Cluster {i}')

# Отображение центроидов
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], color='k', marker='X', s=200, label='Centers')

# Настройка графика
ax.set_title('Кластеризация эмбеддингов с KMeans')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
ax.legend()
plt.show()