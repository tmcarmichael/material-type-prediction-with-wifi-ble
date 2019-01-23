"""
Milestone 2 - 2D Scatter Visual Py
Thomas Carmichael
Networking - COSC6377
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('/home/pmagic/Desktop/netprojectdata.csv')
# print(data.shape)
# data.head()

# 3D list for: Material type, BLE readings, WIFI readings
p1 = data['BLE']
p2 = data['WIFI']
p3 = data['MatNum']
X = np.array(list(zip(p1, p2, p3)))
# print(X)

# Plot data without Kmeans prediction
for x, y, z in X:
    if z == 1:
        plt.scatter(x, y, c='red', s=20, marker='+')
    if z == 2:
        plt.scatter(x, y, c='blue', s=20, marker='*')
    if z == 3:
        plt.scatter(x, y, c='green',s=20, marker='x')
    if z == 4:
        plt.scatter(x, y, c='purple',s=20, marker='^')
    if z == 5:
        plt.scatter(x, y, c='orange',s=20, marker='4')

# KMeans fitting
km = KMeans(n_clusters=5, algorithm='auto', init='k-means++', max_iter=10000, tol=0.0001, verbose=1)
km = km.fit(X)
labels = km.predict(X)
C = km.cluster_centers_

# Axis information for plot
plt.title('RSSI Measurements of BLE and WIFI Protocol with 5 clusters')
plt.ylabel('WIFI 2.4GHz RSSI')
plt.xlabel('BLE 2.4GHz RSSI')

# Organize data for labels and legend
mats = ['No Material','Cardboard','Pillow','Glass','Wood']
colors = ['red','blue','green','purple','orange']
LegendC = list(zip(mats, colors))

# Show KMeans Clustering Prediction
for i in range(len(C)):
    plt.scatter(C[i, 0], C[i, 1], c=colors[i], alpha=0.2, s=9001)

# Create plot legend
for i in LegendC:
    plt.scatter([], [], [], c=i[1], label=i[0])
plt.legend()

# Set Plot Axis bounds
plt.ylim(35, 60) 
plt.xlim(60, 80)

# Show plot
plt.show()
