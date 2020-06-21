#!/usr/bin/python

import sys
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout

# graph drawing options
def draw(graph):
    pos=graphviz_layout(graph, prog='dot')
    nx.draw_networkx(graph,pos,font_color='white',font_size=15)
    labels = nx.get_edge_attributes(graph,'weight')
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels,font_size=20)

sys.argv[1:] = [int(i) for i in sys.argv[1:]]

# plotting options
plt.figure(figsize=(8,8))

# construct graph
g = nx.DiGraph();

for i in sys.argv[1:]:
    g.add_node(i)

for i in range(len(sys.argv[1:])):
    if 2*i+1 >= len(sys.argv[1:]): break 
    g.add_edge(sys.argv[1:][i],sys.argv[1:][2*i+1])
    g.add_edge(sys.argv[1:][i],sys.argv[1:][2*i+2])
    
#buildbintree(g,sys.argv[1:])

draw(g)
plt.savefig("graph.png")
