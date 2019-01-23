"""
Milestone 2 - Confusion Matrix Heatmap using Seaborn
Thomas Carmichael
Networking - COSC6377
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# CMatrix from Euclidean distance of actual points with label to nearest clusters
cmatrix = [[0,3,0,0,22], 
        [0,7,3,15,0], 
        [7,5,11,2,0], 
        [7,14,1,2,1], 
        [8,2,13,2,0]]

# Set Axis'
matClassesC = ['No Material','Cardboard','Pillow','Glass','Wood']
matClassesR = ['No Material','Cardboard','Pillow','Glass','Wood']
matClassesC.reverse()

# Build Data frame with Confusion Matrix
df_cm = pd.DataFrame(cmatrix, index = [i for i in matClassesR], columns = [i for i in matClassesC])
plt.figure(figsize = (8,5))
sns.heatmap(df_cm, cmap='plasma', annot=True)

# Format plot
plt.title('Confusion Matrix Heatmap')
plt.ylabel('Predicted Class Label')
plt.xlabel('Actual Class Labels')

# Show plot
plt.show()