# Kmeans clustering algorithm animated demo

# Generated and adjusted using ChatGPT (the code may not be 100% optimal and readable)
# Note: The parameters (centroid initial positions, shape of data, ...) 
#   are intentionally set unfavorably for the Kmeans algo so that it takes 
#   more steps to converge and by this make the clustering process better 
#   visible when animated.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.utils import shuffle

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_clusters = 3
points_per_cluster = 150
num_steps = 15

# Custom cluster specifications
cluster_specs = [
    {"center": [0, 0], "std": [[10, 0], [0, 2]]},     # Horizontally elongated
    {"center": [15, 5], "std": [[3, 0], [0, 3]]},     # Compact
    {"center": [5, 20], "std": [[2, 0], [0, 8]]}      # Vertically elongated
]

# Generate synthetic data
X_parts = [
    np.random.multivariate_normal(spec["center"], spec["std"], points_per_cluster)
    for spec in cluster_specs
]
X = np.vstack(X_parts)
X = shuffle(X, random_state=42)

# Data bounds for plotting and centroid initialization
x_min, x_max = X[:, 0].min(), X[:, 0].max()
y_min, y_max = X[:, 1].min(), X[:, 1].max()

# Start all centroids at the same point (middle of the space)
initial_point = np.array([[10, 10]])
centroids = np.repeat(initial_point, n_clusters, axis=0)
labels = np.zeros(len(X), dtype=int)

# Plot setup
fig, ax = plt.subplots(figsize=(8, 6))
sc = ax.scatter(X[:, 0], X[:, 1], s=30, color='gray')
centers_plot = ax.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X', label="Centroids")
legend = ax.legend(loc="upper right")
ax.set_xlim(x_min - 5, x_max + 5)
ax.set_ylim(y_min - 5, y_max + 5)

# Centroid history for optional future trail plotting
centroid_history = [centroids.copy()]

# Update function
def update(frame):
    global centroids, labels, centroid_history

    if frame == -1:
        # Initial frame — show original centroid position
        sc.set_color('gray')
        centers_plot.set_offsets(centroids)
        ax.set_title("Initial centroid positions")
        return

    # Step 1: Assign points to nearest centroid
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    labels = np.argmin(distances, axis=1)

    # Step 2: Update centroids
    new_centroids = np.array([
        X[labels == i].mean(axis=0) if np.any(labels == i) else centroids[i]
        for i in range(n_clusters)
    ])

    centroids = new_centroids
    centroid_history.append(centroids.copy())

    # Update visuals
    sc.set_color([plt.cm.tab10(label) for label in labels])
    centers_plot.set_offsets(centroids)
    ax.set_title(f"K-means Step {frame + 1}")

# Create animation (start with frame -1 to show initial state)
frames = [-1] + list(range(num_steps))
anim = FuncAnimation(fig, update, frames=frames, interval=800, repeat=False)

plt.tight_layout()
plt.show()
