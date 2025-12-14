import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Sample 2D data, produces 100 randomly generated points in a matrix
X = np.random.uniform(0, 10, (100, 2))

# Apply K-Means with K=2
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Get centroids and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting
colors = ["r", "b"]
for i in range(len(X)):
    plt.scatter(X[i][0], X[i][1], color=colors[labels[i]])

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=200, c="black", label="Centroids")
plt.title("K-Means Clustering (K=2)")
plt.legend()
plt.grid(True)
plt.show()

# Example of Squared Euclidean Distance
# From first point to its centroid
point = X[0]
centroid = centroids[labels[0]]
squared_dist = np.sum((point - centroid) ** 2)
print(f"Squared Euclidean distance from point {point} to its centroid: {squared_dist:.2f}")
