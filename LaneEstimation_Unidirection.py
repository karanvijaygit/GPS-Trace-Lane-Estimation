import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
def road_lane_estimation_unidir(df_comb,roadid, k):
    df = df_comb[df_comb['RoadId'] == roadid]
    colors = ['b', 'g', 'k', 'm', 'y', 'c','w']
    if df.iloc[0, 9] == 'Forward':
        X_f = np.array(df.iloc[:, 2:4])
        kmean_f = KMeans(n_clusters=k)
        kmean_f.fit(X_f)
        df['labels'] = kmean_f.labels_
        fig, ax = plt.subplots(figsize=(20, 10))


        # Plotting Forward lanes clusters
        ax.title.set_text('Forward Lane Cluster Plot')
        for i in range(k):
            ax.scatter(df[df['labels'] == i]['Lattitude'].values, df[df['labels'] == i]['Longitude'].values,
                        color=colors[i])

        # Plotting Forward lanes cluster centroids
        for i in range(k):
            ax.plot(kmean_f.cluster_centers_[i][0], kmean_f.cluster_centers_[i][1], 'rx')
        plt.show()

    elif df.iloc[0, 9] == 'Backward':
        X_b = np.array(df.iloc[:, 2:4])
        kmean_b = KMeans(n_clusters=k)
        kmean_b.fit(X_b)
        df['labels'] = kmean_b.labels_
        fig, ax = plt.subplots(figsize=(20, 10))
        # Plotting Forward lanes clusters
        ax.title.set_text('Backward Lane Cluster Plot')
        for i in range(k):
            ax.scatter(df[df['labels'] == i]['Lattitude'].values, df[df['labels'] == i]['Longitude'].values,
                       color=colors[i])

        # Plotting Forward lanes cluster centroids
        for i in range(k):
            ax.plot(kmean_b.cluster_centers_[i][0], kmean_b.cluster_centers_[i][1], 'rx')

        plt.show()