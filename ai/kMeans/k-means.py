import matplotlib.pyplot as plt

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# to see the plot
# plt.scatter(x,y)
# plt.show()

data = list(zip(x,y))

"""to find the number of cluster i use elbow method to see which no of cluster is best fitted"""
# initial = []
from sklearn.cluster import KMeans
# for i in range(1,11):
#     kmeans = KMeans(n_clusters=i)
#     kmeans.fit(data)
#     initial.append(kmeans.inertia_)
#
# plt.plot(range(1,11),initial,marker='*')
# plt.title("Elbow method")
# plt.xlabel("number of cluster")
# plt.ylabel("Inertia")
# plt.show()
# =======================================
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x,y,c=kmeans.labels_)
plt.show()
plt.savefig("Kmeans_cluster.jpg")