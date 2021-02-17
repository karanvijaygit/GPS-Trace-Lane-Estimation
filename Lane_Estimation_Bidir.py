import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
def road_lane_estimation_bidir(df_comb,roadid, kf, kb):
    df = df_comb[df_comb['RoadId'] == roadid]
    if df.iloc[0, 9] == 'Both':
        df_f = df[df['DirOfTravel'] == -roadid]
        df_b = df[df['DirOfTravel'] == roadid]
        X_f = np.array(df_f.iloc[:, 2:4])
        X_b = np.array(df_b.iloc[:, 2:4])
        kmean_f = KMeans(n_clusters=kf)
        kmean_f.fit(X_f)
        df_f['labels'] = kmean_f.labels_
        kmean_b = KMeans(n_clusters=kb)
        kmean_b.fit(X_b)
        df_b['labels'] = kmean_b.labels_
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
        fig.suptitle('Forward and Backward Direction Clusters Plotting')
        colors = ['b', 'g','k','m','y','c','w']

        # Plotting Forward lane clusters
        ax1.title.set_text('Forward Lane Cluster Plot')
        for i in range(kf):
            ax1.scatter(df_f[df_f['labels'] == i]['Lattitude'].values, df_f[df_f['labels'] == i]['Longitude'].values,
                        color=colors[i])

        # Plotting Forward lane clusters
        for i in range(kb):
            ax2.scatter(df_b[df_b['labels'] == i]['Lattitude'].values, df_b[df_b['labels'] == i]['Longitude'].values,
                        color=colors[i])

        # Plotting Forward lanes cluster centroids
        for i in range(kf):
            ax1.plot(kmean_f.cluster_centers_[i][0], kmean_f.cluster_centers_[i][1], 'rx')

        # Plotting Backward lanes cluster centroids
        for i in range(kb):
            ax2.plot(kmean_b.cluster_centers_[i][0], kmean_b.cluster_centers_[i][1], 'rx')

        plt.show()
    else:
        print("Pls. use this function only for bi-directional road")