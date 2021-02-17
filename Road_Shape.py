import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def plot_road_shape(df_comb,roadid):
    df = df_comb[df_comb['RoadId']==roadid]
    max_coord_num = max(df['geometry.coordinates'].map(lambda x: len(x)))
    num_pairs_coord = int(max_coord_num/3)
    road_coord = np.array(df.iloc[0,8]).reshape(num_pairs_coord,3)
    road_coord_df = pd.DataFrame(road_coord,columns=['x','y','z'])
    plt.plot(road_coord_df['y'].values,road_coord_df['x'].values)
    plt.plot(road_coord_df['y'].values,road_coord_df['x'].values,'rx')
    plt.show()