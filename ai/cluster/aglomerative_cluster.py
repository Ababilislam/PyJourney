#Three lines to make our compiler able to draw:
import sys

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import matplotlib
matplotlib.use('Agg')

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig("data.png")
# sys.stdout.flush()
