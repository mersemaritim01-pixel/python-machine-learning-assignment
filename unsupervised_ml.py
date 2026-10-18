from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
#preparing customers monthly spending and monthy visits
X=[
    [1000,2],
    [1500,3],
    [2000,2],
    [5000,6],
    [6000,7],
    [5500,5],
    [12000,12],
    [15000,14],
    [13000,11],
    [3000,4]]
#use StandardScaler to scale the spending and visits features
scaler=StandardScaler()
scaled_data=scaler.fit_transform(X)
#create a model
model=KMeans(n_clusters=3, random_state=42, n_init=10)
#train the model
model.fit(scaled_data)
#predicting the clusters
groups=model.predict(scaled_data)
#display the cluster assigned to each customer
assigned_cluster=model.labels_
print("Assigned Clusters for each customer:")
for i, cluster in enumerate(assigned_cluster):
    print(f"Customer {i+1}: Cluster {cluster}")
#display the total number of customers in each cluster
print("\nTotal number of customers in each cluster:")
for cluster in range(3):
    count = list(assigned_cluster).count(cluster)
    print(f"Cluster {cluster}: {count} customers")

#visualizing the clusters
import matplotlib.pyplot as plt

plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=assigned_cluster, cmap='viridis')
plt.xlabel('Scaled Spending')
plt.ylabel('Scaled Visits')
plt.title('Customer Segments')
plt.show()