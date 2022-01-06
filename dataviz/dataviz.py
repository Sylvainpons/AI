import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import numpy as np 

df = pd.read_csv("data/clean_timetables.csv")

def datavisualization(df):
    net=Network()
    i=0
    dict_gare={}
    unique_gares = list(set(np.concatenate((list(df["destination"]), list(df["origin"])), axis=None)))
    for gare in unique_gares :
        dict_gare[gare]=i
        net.add_node(i,label=gare)
        i+=1

    for i in df.index:
        dep=dict_gare[df['origin'][i]]
        arr=dict_gare[df['destination'][i]]
        w=int(df['length'][i])
        net.add_edge(dep,arr,value=w)
        
    net.repulsion(node_distance=400, spring_length=400)
    net.show_buttons(filter_=True)
    net.show('dataviz/edges_with_weights.html')

datavisualization(df)