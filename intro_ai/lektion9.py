from sklearn.cluster import KMeans, DBSCAN
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np

""" blobs_data = pd.read_csv("datasets/blobs.csv")
noisy_circles_data = pd.read_csv("datasets/noisy_circles.csv")



X_blob = blobs_data[["Feature1", "Feature2"]].values
labels_blobs = blobs_data['labels'].values

X_noisy = noisy_circles_data[["Feature1", "Feature2"]].values
labels_noisy = noisy_circles_data['labels'].values

scaler = StandardScaler()
X_blob_scaled = scaler.fit_transform(X_blob)
X_noisy_scaled = scaler.fit_transform(X_noisy)

plt.scatter(X_blob_scaled[:, 0], X_blob_scaled[:, 1], c=labels_blobs, cmap='viridis')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Blobs Dataset")
plt.colorbar(label="Label")
plt.show()


plt.scatter(X_noisy_scaled[:, 0], X_noisy_scaled[:, 1], c=labels_noisy, cmap='viridis')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Noisy Circles Dataset")
plt.colorbar(label="Label")
plt.show() 

k = 3  # Number of clusters for KMeans

kmeans_blob = KMeans(n_clusters=k, random_state=42)
kmeans_labels_blob = kmeans_blob.fit_predict(X_blob_scaled)

dbscan_blob = DBSCAN(eps=0.205, min_samples=5)
dbscan_labels_blob = dbscan_blob.fit_predict(X_blob_scaled)

kmeans_noisy = KMeans(n_clusters=2, random_state=42)
kmeans_labels_noisy = kmeans_noisy.fit_predict(X_noisy_scaled)

dbscan_noisy = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels_noisy = dbscan_noisy.fit_predict(X_noisy_scaled)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
plots = [
	(axes[0, 0], X_blob_scaled, kmeans_labels_blob, "KMeans — Blobs", kmeans_blob.cluster_centers_),
	(axes[0, 1], X_blob_scaled, dbscan_labels_blob, "DBSCAN — Blobs", None),
	(axes[1, 0], X_noisy_scaled, kmeans_labels_noisy, "KMeans — Noisy Circles", kmeans_noisy.cluster_centers_),
	(axes[1, 1], X_noisy_scaled, dbscan_labels_noisy, "DBSCAN — Noisy Circles", None),
]

for ax, data, cluster_labels, title, centers in plots:
	ax.scatter(data[:, 0], data[:, 1], c=cluster_labels, cmap="viridis", s=20)
	if centers is not None:
		ax.scatter(centers[:, 0], centers[:, 1], marker="x", s=120, linewidths=3, color="red", label="Centroids")
		ax.legend()
	ax.set_title(title)
	ax.set_xlabel("Feature 1 (scaled)")
	ax.set_ylabel("Feature 2 (scaled)")

fig.tight_layout()
plt.show()

print("KMeans Labels for Blobs Dataset:", kmeans_labels_blob)
print("DBSCAN Labels for Blobs Dataset:", dbscan_labels_blob)
print("KMeans Labels for Noisy Circles Dataset:", kmeans_labels_noisy)
print("DBSCAN Labels for Noisy Circles Dataset:", dbscan_labels_noisy) """


mall_data = pd.read_csv("datasets/mall_customers.csv")

X_mall = mall_data[["Annual Income (k$)", "Spending Score (1-100)"]].values

plt.scatter(X_mall[:, 0], X_mall[:, 1], s=40, alpha=0.7)
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Mall Customers")
plt.grid(True, alpha=0.3)
plt.show()

standard_scaler = StandardScaler()
X_mall_scaled = standard_scaler.fit_transform(X_mall)

# Calculate silhouette scores for candidate cluster counts.
k_values = range(2, min(10, len(X_mall_scaled) - 1) + 1)
silhouette_scores = []

for k in k_values:
	kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
	cluster_labels = kmeans.fit_predict(X_mall_scaled)
	silhouette_scores.append(silhouette_score(X_mall_scaled, cluster_labels))

plt.plot(k_values, silhouette_scores, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Method for Mall Customers")
plt.xticks(list(k_values))
plt.grid(True, alpha=0.3)
plt.show()

best_k = list(k_values)[int(np.argmax(silhouette_scores))]
print(f"Best k by silhouette score: {best_k}")

kmeans_mall = KMeans(n_clusters=best_k, random_state=42, n_init=10)
mall_labels = kmeans_mall.fit_predict(X_mall_scaled)

# Describe each cluster using its average values in the original units.
mall_profiles = mall_data[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].copy()
mall_profiles["Cluster"] = mall_labels
cluster_summary = mall_profiles.groupby("Cluster").agg(
	Customers=("Annual Income (k$)", "size"),
	Mean_Age=("Age", "mean"),
	Mean_Income=("Annual Income (k$)", "mean"),
	Mean_Spending_Score=("Spending Score (1-100)", "mean"),
).round(1)

print("\nMall customer cluster descriptions:")
for cluster, profile in cluster_summary.iterrows():
	income_level = "high" if profile["Mean_Income"] >= mall_data["Annual Income (k$)"].mean() else "low"
	spending_level = "high" if profile["Mean_Spending_Score"] >= mall_data["Spending Score (1-100)"].mean() else "low"
	print(
		f"Cluster {cluster}: {int(profile['Customers'])} customers, "
		f"mean age {profile['Mean_Age']:.1f}, "
		f"{income_level} income (mean ${profile['Mean_Income']:.1f}k) and "
		f"{spending_level} spending (mean score {profile['Mean_Spending_Score']:.1f})."
	)

mall_centers = standard_scaler.inverse_transform(kmeans_mall.cluster_centers_)
plt.scatter(X_mall[:, 0], X_mall[:, 1], c=mall_labels, cmap="viridis", s=40, alpha=0.7)
plt.scatter(mall_centers[:, 0], mall_centers[:, 1], marker="X", s=200, color="red", label="Centroids")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title(f"Mall Customer Clusters (k={best_k})")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Compare age with each clustering feature, colored by cluster assignment.
fig = plt.figure(figsize=(18, 5))
axes = [fig.add_subplot(131), fig.add_subplot(132)]
axes[0].scatter(mall_data["Age"], X_mall[:, 0], c=mall_labels, cmap="viridis", s=40, alpha=0.7)
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Annual Income (k$)")
axes[0].set_title("Age vs. Annual Income")
axes[1].scatter(mall_data["Age"], X_mall[:, 1], c=mall_labels, cmap="viridis", s=40, alpha=0.7)
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Spending Score (1-100)")
axes[1].set_title("Age vs. Spending Score")
ax_3d = fig.add_subplot(133, projection="3d")
ax_3d.scatter(
	mall_data["Age"], X_mall[:, 0], X_mall[:, 1],
	c=mall_labels, cmap="viridis", s=40, alpha=0.7,
)
ax_3d.set_xlabel("Age")
ax_3d.set_ylabel("Annual Income (k$)")
ax_3d.set_zlabel("Spending Score (1-100)")
ax_3d.set_title("Age, Income, and Spending Score")
for ax in axes:
	ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()



