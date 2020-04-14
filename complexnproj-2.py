# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:41:58 2019

@author: dai
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np
import pickle
inputpath = 'D:\\cumulative_2009-04-28.gml'
H = nx.read_gml(inputpath,label='id')

nodes_n = nx.number_of_nodes(H)
nodes_color=[0]*nodes_n
for i in range(nodes_n):
    H.nodes[i]['status']=0
    H.nodes[i]['time']=0

list(H.nodes(data=True))

firsts=134
#firsts=random.randint(0,nodes_n)
H.nodes[firsts]['status']=1
H.nodes[firsts]['time']=1
Fneighbor=H.__getitem__(firsts)
FD=len(Fneighbor)
print(Fneighbor)
print(FD)

nodes_nei=[]
dictfile=open("posfile",'rb')
pos=pickle.load(dictfile)
p1=0.5
p2=0.7
p3=0.9
p4=0.6
p5=0.8
p6=0.95

for i in range(10):
    infn=1
    infn2=0
    for u in range(nodes_n):
        node_neighbor=H.__getitem__(u)
        for v in range(u+1,nodes_n):
            if v in node_neighbor:
                edge_weight=H.get_edge_data(u,v)
                u_status = H.nodes[u]['status']
                v_status = H.nodes[v]['status']
                edge_w=int(edge_weight['weight'])
                if u_status==0 and v_status == 0:
                    pass
                elif u_status==0 and v_status == 1:
                    
                    if edge_w<=3:
                        np.random.seed(0)
                        p = np.array([1-p1, p1])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[u]['status']=index
                        nodes_color[u] = index
                        
                            
                    elif 3<edge_w<=10:
                        np.random.seed(0)
                        p = np.array([1-p2,p2])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[u]['status']=index
                        nodes_color[u] = index

                            
                    else:
                        np.random.seed(0)
                        p = np.array([1-p3,p3])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[u]['status']=index
                        nodes_color[u] = index

                            
                elif u_status==1 and v_status == 0:
                    H.nodes[u]['time']=H.nodes[u]['time']+1
                    if edge_w<=3:
                        np.random.seed(0)
                        p = np.array([1-p1, p1])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[v]['status']=index
                        nodes_color[v] = index

                            
                    elif 3<edge_w<=10:
                        np.random.seed(0)
                        p = np.array([1-p2,p2])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[v]['status']=index
                        nodes_color[v] = index

                            
                    else:
                        np.random.seed(0)
                        p = np.array([1-p3,p3])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[v]['status']=index
                        nodes_color[v] = index

                            
                elif u_status==0 and v_status == 2:
                    
                    if edge_w<=3:
                        np.random.seed(0)
                        p = np.array([1-p4, p4])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[u]['status']=index
                        nodes_color[u] = index
                        
                            
                    elif 3<edge_w<=10:
                        np.random.seed(0)
                        p = np.array([1-p5,p5])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[u]['status']=index
                        nodes_color[u] = index

                            
                    else:
                        np.random.seed(0)
                        p = np.array([1-p6,p6])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[u]['status']=index
                        nodes_color[u] = index

                            
                elif u_status==2 and v_status == 0:
                    if edge_w<=3:
                        np.random.seed(0)
                        p = np.array([1-p4,p4])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[v]['status']=index
                        nodes_color[v] = index

                            
                    elif 3<edge_w<=10:
                        np.random.seed(0)
                        p = np.array([1-p5,p5])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[v]['status']=index
                        nodes_color[v] = index

                            
                    else:
                        np.random.seed(0)
                        p = np.array([1-p6,p6])
                        index = np.random.choice([0, 1], p = p.ravel())
                        H.nodes[v]['status']=index
                        nodes_color[v] = index

                
                else:
                    pass
                
    for u in range(nodes_n):
        if H.nodes[u]['status']==1:
            H.nodes[u]['time']=H.nodes[u]['time']+1
            infn=infn+1
        elif H.nodes[u]['status']==2:
            infn2 = infn2+1

        if H.nodes[u]['status']==1 and H.nodes[u]['time']>=2:
            np.random.seed(0)
            p = np.array([0.1,0.9])
            index = np.random.choice([1, 2], p = p.ravel())
            H.nodes[u]['status']=index
            nodes_color[u] = index

    print('suspe is %s' %infn)
    print('infect is %s' %infn2)
    nodes_color[firsts] = 1.5
    plt.figure(figsize=(20,20))
    nx.draw_networkx(H,pos,node_size=50,alpha=0.9,cmap = plt.get_cmap('jet'),with_labels=False,node_color=nodes_color)
