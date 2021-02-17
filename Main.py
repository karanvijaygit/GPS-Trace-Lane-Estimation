import pandas as pd
import numpy as np
import geojson as gj
from pandas import json_normalize
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import Lane_Estimation_Bidir as bidr
import LaneEstimation_Unidirection as unidir
import Road_Shape as rshape
import Silhouette_Score as silsc
import Road_Shape_Coord_Clean as rshape_coord_clean


df_gps_trace = pd.read_csv('road-gps-data.csv')
with open('roads.json') as f:
    gjf = gj.load(f)
lst = []
for i in range(len(gjf['features'])):
    lst.append(json_normalize(gjf['features'][i]))

df_roads = pd.DataFrame()
for i in range(len(gjf['features'])):
    df_roads = df_roads.append(lst[i])

df_roads['geometry.coordinates'] = df_roads['geometry.coordinates'].map(lambda x: rshape_coord_clean.coord_clean(x))

# Renaming id to RoadId to match with other Gps Trace table column
df_roads = df_roads.rename(columns={'id':'RoadId'})

# Converting object dtype to Numeric for RoadId Column
df_roads['RoadId']=pd.to_numeric(df_roads['RoadId'])

df_comb = df_gps_trace.merge(df_roads,on='RoadId')
df_comb = df_comb.drop(['type','geometry.type'],axis=1)
#print(df_comb['RoadId'].value_counts())
# rshape.plot_road_shape(df_comb,8460193543)
# silsc.Silhouette_Score_Eval(8460193543,df_comb)
unidir.road_lane_estimation_unidir(df_comb,8460193543,5)
# bidr.road_lane_estimation_bidir(df_comb,8460193543,2,4)