# Classifying materials with different wireless protocols
<br>

#### File Index:
 	Networking Project Report.pdf    -- Primary Report PDF
	Networking Project Data.csv	 -- Data used for K-Means Clustering
	2DScatterKNNCluster.png          -- 2D K-means Clustering Scatter Image
 	2DScatterKNNCluster.py           -- 2D K-means Clustering Python
	3DScatterKNNCluster.png          -- 3D K-means Clustering Scatter Image Normal Clusters
	3DScatterKNNClusterClear.png     -- 3D K-means Clustering Scatter Image Clear Clusters
 	3DScatterKNNCluster.py           -- 3D K-means Clustering Python
	CMatrixHeatmap.png		 -- Confusion Matrix Image
	CMatrixHeatmap.py		 -- Confusion Matrix Python


#### Introduction:
BLE and WIFI 2.4GHz radio RSSI material detection with 5 material classes.
See 'Networking Project Report.pdf' file in repo for literature review, introduction of the problem, and unique contribution I have tried to make.
<br>

#### Design: 
A transmitter was placed in a box designed to only transmit wireless signal through a selected material class (no material, wood, pillow, glass, thick cardboard). A reciever was placed 6 feet away from the transmitter. Using this setup, the material type can be isolated as the cause in changes in RSSI, measured in dBm, between the pair. Alternating the protocol or hardware used may yield enough information to accurately classify the material between the objects. 
<br>

#### Implementation:
Using a plastic box with dimensions l,h,w = "14,"10,"10, wrapped with alumunim foil allowed for most transmitter signals to be reflected. One opening was left unwrapped by aluminum and instead was covered by each material class for data collection. The two protocols used were BLE and WIFI both 2.4GHz radios. Nordic's nRF52840 dongle advertised BLE to a Samsung Galaxy S7 Edge Android phone for the BLE measurements. The BLE Scanner app was used to record measurements. A university issued Meru Networks wireless access point advertised 2.4GHz wireless signal to a ThinkPad X260 running Ubuntu 18.04 OS. ```iwconfig winterface | grep -i --color signal``` was used in data collection. NOTE: the nRF board's 802.15.4 required another nRF DK board as a pair, and the rest of the protocols weren't usable at 6 feet distance. I have flashed the board for 802.15.4 use and can explain setup and use if needed. For futher WIFI radar experimentation I suggest MIMO devices to collect object shape information (such as 3x  omnidirectional dual band rubber duckys). More information on improvements to experimental design can be found in 'Networking Project Report.pdf'.
<br>

#### Evaluation:
The key question in this experiment is can material classes be reliably classified with only wireless RSSI fluxuations. Clustering algorithms allow us to classify d-dimensional data points into groups. Therefore a K-means Clustering algorithm was chosen to investigate the possibility of accurately grouping all data points into n clusters of material types. As can be seen below, the clusters of materials are difficult to separate, even over 10,000 iterations of the K-means algorithm. The 'No Material' class can be differentiated from the four other material classes, however the model needs additional data to examine the possibility of additional data allowing for clustering. Below we'll take a look at a view visualizations of a 5 cluster K-means algorithm running 10,000 iterations. Additional information on how further research can better classify the material groups is provided in the conclusion as well as the PDF report.
<br><br>

## 2D K-Means Clustering, 10,000 iterations
![2D Scatter](https://github.com/tmcarmichael/material-type-prediction-with-wifi-ble/blob/master/2DScatterKNNCluster.png)
Using Scikit-Learn: see **2DScatterKNNCluster.py** for more detail. *KMeans(n_clusters=5, algorithm='auto', init='k-means++', max_iter=10000, tol=0.0001, verbose=1)*
<br><br><br>

## 3D K-Means Clustering, 10,000 iterations
![3D Scatter](https://github.com/tmcarmichael/material-type-prediction-with-wifi-ble/blob/master/3DScatterKNNCluster.png)
<br>

Using Scikit-Learn: see **3DScatterKNNCluster.py** for more detail. **NOTE**: The large translucent cluster circles color isn't indicative of the color on the legend, it is indicative of the position of a cluster's center after x iterations. K-Means initializes clusters in random locations. *KMeans(n_clusters=5, algorithm='auto', init='k-means++', max_iter=10000, tol=0.0001, verbose=1)*
<br><br><br>

## 3D K-Means Clustering (Clear, and another angle), 10,000 iterations
![3D Scatter](https://github.com/tmcarmichael/material-type-prediction-with-wifi-ble/blob/master/3DScatterKNNClusterClear.png)
Using Scikit-Learn: see **3DScatterKNNCluster.py** for more detail. *KMeans(n_clusters=5, algorithm='auto', init='k-means++', max_iter=10000, tol=0.0001, verbose=1)*
<br><br>

## Confusion Matrix Heatmap
![Confusion Matrix](https://github.com/tmcarmichael/material-type-prediction-with-wifi-ble/blob/master/CMatrixHeatmap.png)
<br>
Using Seaborn with Matplotlib: see **CMatrixHeatmap.py** for more detail. 
<br>

Using 25 samples from each material group, a confusion matrix allows for an understanding of the accuracy of the clustering model. As illustrated by the confusion matrix, the presence or absence of a material can be detected reliably, with about 22/25 or 88% accuracy. However, the accuracy drops when trying to differentiate two material types.  Methodological steps mentioned in the literature review PDF offer ways to both differentiate object type AND object shape. 
<br>

#### Conclusions: 
As the above Confusion Matrix and K-Means Clustering clearly demonstrate, object detection with wireless radio is a difficult task to accomplish without seriously reducing the scope or power of object classification. My initial goals were slightly ambitious, and procedural changes need to be made to make accurate classifications. I hoped that using different signal protocols such as Bluetooth and WIFI would be sufficient. While I'm not able to predict an object's material class from RSSI with a high degree of accuracy, I can detect the presense or absense of an object with my model. In the PDF literature review I present some ways in which researchers have increased the feature space to allow for more robust models (using CSI data, Multipath Effect with MIMO devices, using clear classification classes such as simply Metal, Liquid, Other, and other techniques.) With the IOT movement wireless detection, especially using 2.4GHz commodity radios, will have a growing set of use cases. I enjoyed this project and reading into the current literature, thanks to Milad and Dr. Gnawali for feedback and help.

