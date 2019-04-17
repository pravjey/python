import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import random

# Reading CSV file dataset into Pandas dataframe

file_csv = "E:\MSc Data Science\Data Science Techniques and Applications\Coursework\\tweets.csv"
df = pd.read_csv(file_csv)

# Selecting three dimensions for analysis and showing number of items in each sub dataframe

print("\n")
print("Selecting datafram dimensions for analysis")
print("================================e=========")
print("\n")

followers = df["followers"]
print("Number of follower counts:", len(followers))

status = df["numberstatuses"]
print("Number of status counts:", len(status))

timestamp = pd.to_datetime(df["time"])
print("Number of timestamps:", len(timestamp))

# Converted dataframe subsets in NumPy arrays, then converted the Numpy arrays into lists for purposes of speed

followers = np.array(followers.values)
status = np.array(status.values)
timestamp = np.array(timestamp.values)

followers = followers.tolist()
status = status.tolist()
timestamp = timestamp.tolist()

# Plotted 2D and 3D scatterplots to show distribution of data  

print("\n")
print("Plotting 2D pair of scatterplots")
print("================================")
print("\n")

plt.figure(figsize=(8, 8), dpi=80)
plt.scatter(timestamp,followers)
plt.title("What was the tweeter's follower count at time of publication of tweet")
plt.xlabel("Timestamp of tweet")
plt.ylabel("Follower count")
plt.show()

plt.figure(figsize=(8, 8), dpi=80)
plt.scatter(timestamp,status)
plt.title("What was the tweeter's status count at time of publication of tweet")
plt.xlabel("Timestamp of tweet")
plt.ylabel("Status count")
plt.show()

plt.figure(figsize=(8, 8), dpi=80)
plt.scatter(followers,status) 
plt.title("Comparison between follower and status count at time of publication of tweet")
plt.xlabel("Follower count")
plt.ylabel("Status count")
plt.show()

print("\n")
print("Plotting 3D scatterplot")
print("=======================")
print("\n")

fig = plt.figure(figsize=(8, 8), dpi=80)
ax = fig.add_subplot(111, projection='3d')

ax.scatter(timestamp, followers, status)

ax.set_xlabel("timestamp of tweet")
ax.set_ylabel("follower count")
ax.set_zlabel("status count")

plt.show()

# Undertaking Principle Component Analysis
# Source: https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60 

features = ["followers", "numberstatuses"]

 
x = df.loc[:, features].values
y = df.loc[:,['username']].values
x = StandardScaler().fit_transform(x)

pca = PCA(n_components = 2)

principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ["principal component 1","principal component 2"])
finalDf = pd.concat([principalDf, df[["username"]]],axis=1)

fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel("Principal Component 1", fontsize = 10)
ax.set_ylabel("Principal Component 2", fontsize = 10)
ax.set_title("2 component PCA", fontsize = 20)

targets = df["username"].unique()
targets = np.array(targets).tolist()
for target in targets:
    indicesToKeep = finalDf['username'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = "r"
               , s = 50)
#ax.legend(targets)
ax.grid()

plt.show()

