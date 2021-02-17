import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
def Silhouette_Score_Eval(roadid,df_comb):
    kmeans_kwargs = {
        "init": "random",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 42,
    }
    df = df_comb[df_comb['RoadId'] == roadid]
    if df.iloc[0, 9] == 'Both':
        df_f = df[df['DirOfTravel'] == -roadid]
        df_b = df[df['DirOfTravel'] == roadid]
        X_f = np.array(df_f.iloc[:, 2:4])
        X_b = np.array(df_b.iloc[:, 2:4])
        silhouette_coefficients_f = []
        silhouette_coefficients_b = []
        for k in range(2, 11):
            kmeans_f = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans_b = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans_f.fit(X_f)
            kmeans_b.fit(X_b)
            score_f = silhouette_score(X_f, kmeans_f.labels_)
            silhouette_coefficients_f.append(score_f)
            score_b = silhouette_score(X_b, kmeans_b.labels_)
            silhouette_coefficients_b.append(score_b)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
        plt.style.use("fivethirtyeight")
        plt.xlabel("Number of Clusters")
        plt.ylabel("Silhouette Score_Forward Clusters")
        plt.xticks(range(2, 11))
        ax1.title.set_text('Forward Lane Cluster Sillhouete Score')
        ax1.plot(range(2, 11), silhouette_coefficients_f)
        ax2.title.set_text('Backward Lane Cluster Sillhouete Score')
        ax2.plot(range(2, 11), silhouette_coefficients_b)
        plt.show()

    elif df.iloc[0, 9] == 'Forward':
        X_f = np.array(df.iloc[:, 2:4])
        silhouette_coefficients_f = []
        for k in range(2, 11):
            kmeans_f = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans_f.fit(X_f)
            score_f = silhouette_score(X_f, kmeans_f.labels_)
            silhouette_coefficients_f.append(score_f)
        fig, ax = plt.subplots(figsize=(20, 10))
        plt.style.use("fivethirtyeight")
        plt.xlabel("Number of Clusters")
        plt.ylabel("Silhouette Score_Forward Clusters")
        plt.xticks(range(2, 11))
        ax.plot(range(2, 11), silhouette_coefficients_f)
        plt.show()

    else:
        X_b = np.array(df.iloc[:, 2:4])
        silhouette_coefficients_b = []
        for k in range(2, 11):
            kmeans_b = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans_b.fit(X_b)
            score_b = silhouette_score(X_b, kmeans_b.labels_)
            silhouette_coefficients_b.append(score_b)
        fig, ax = plt.subplots(figsize=(20, 10))
        plt.style.use("fivethirtyeight")
        plt.xlabel("Number of Clusters")
        plt.ylabel("Silhouette Score_Backward Clusters")
        plt.xticks(range(2, 11))
        ax.plot(range(2, 11), silhouette_coefficients_b)
        plt.show()