import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

data=pd.read_csv('ex2data3.csv')                                                                        #Reading in the data to be tested
plt.scatter(data['Satisfaction'], data['Loyalty'])                                                      #plotting out the data
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()

x=data.copy()                                                                                           #copying the data so the original data so we don't actually change it
kmeans=KMeans(2)                                                                                        #Setting number of clusters to 2
kmeans.fit(x)                                                                                           #calling the inbuilt kmeans function fit to train the data x
clusters=x.copy()                                                                                       #copying the data from processed x so as to not change the values of x
clusters['Cluster_pred']=kmeans.fit_predict(x)                                                          # adding a new column to cluster and predicting the cluster the value belongs to
plt.scatter(clusters['Satisfaction'],clusters['Loyalty'],c=clusters['Cluster_pred'],cmap='rainbow')     #plotting out the cluster
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()

from sklearn import preprocessing                                                                       #preprocessing the data to be scaled, implemented by sklearn
x_scaled=preprocessing.scale(x)

wcss=[]

'''Implementing the elbow method to 
find the adequate number of clusters'''

for i in range(1,30):
  kmeans=KMeans(i)
  kmeans.fit(x_scaled)
  wcss.append(kmeans.inertia_)
'''Plotting out the number of
clusters vs the wcss value '''
plt.plot(range(1,30),wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

'''Take the x_scaled data and fit it into a cluster of size four and check the result'''