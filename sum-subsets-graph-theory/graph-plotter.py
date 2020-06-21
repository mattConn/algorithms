#!/usr/bin/python

import sys
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout

# graph drawing options
def draw(graph):
    pos=graphviz_layout(graph, prog='dot')
    nx.draw_networkx(graph,pos,font_color='black',font_size=15,node_size=700)

sys.argv[1:] = [int(i) for i in sys.argv[1:]]

# plotting options
plt.figure(figsize=(8,8))

# construct graph
g = nx.DiGraph();

#for i in sys.argv[1:]:
#    g.add_node(i)

for depth in range(len(sys.argv[1:])):
    leftIndex = 2*depth+1
    rightIndex = 2*depth+2

    if leftIndex >= len(sys.argv[1:]): break 

    # for connecting current node to another
    # labelling each node as "depth:data[depth]"
    def joinCurNodeTo(nodeIndex):
        g.add_edge(f'{depth}:{sys.argv[1:][depth]}', f'{nodeIndex}:{sys.argv[1:][nodeIndex]}')
        print(f'JOINING: {depth}:{sys.argv[1:][depth]} TO {nodeIndex}:{sys.argv[1:][nodeIndex]}')

    joinCurNodeTo(leftIndex)
    joinCurNodeTo(rightIndex)
    

draw(g)
plt.savefig("graph.png")
