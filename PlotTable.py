import matplotlib.pyplot as plt
import networkx as nx
import grapth_star
from backtrack import Grafo

G = nx.Graph()

nodes = ["a","b","c","d"]
vertex = [[1,1,0,1],[1,1,1,1],[0,1,1,1],[1,1,1,1]]

mapa = Grafo()
mapa.setNodes(nodes)
mapa.setVertex(vertex)
mapa.colora_node(0)


G.add_nodes_from(nodes, color = "y")
pos = nx.random_layout(G)
color = nx.get_node_attributes(G,'color')


for i in range(0,len(vertex)):
	for j in range(0,len(vertex[i])):
		if vertex[i][j] == 1:
			G.add_edge(nodes[i],nodes[j])

for i in range(0,len(nodes)):
	G.node[listaNodes[i]]['color'] = mapa.getColor(i)
	nx.draw(G,pos,node_size = 1000,nodelist = nodes[i],node_color = color[nodes[i]])


plt.axis('off')
plt.show()
