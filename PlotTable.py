import matplotlib.pyplot as plt
import networkx as nx
import sys
from backtrack import Grafo

if len(sys.argv) < 2:
    exit("ta faltando coisa")

filename = sys.argv[1]

grafos = __import__("grafos."+filename, globals(), locals(), [filename, filename], 0)

mapa = Grafo()
mapa.setNodes(grafos.nodes)
mapa.setVertex(grafos.vertex)

nodes = grafos.nodes
vertex = grafos.vertex

if mapa.colora_node(0):
    print("tudo ok")
else:
    print("não deu solução")

G = nx.Graph()

G.add_nodes_from(grafos.nodes, color = "y")
pos = nx.random_layout(G)
color = nx.get_node_attributes(G,'color')


for i in range(0,len(grafos.vertex)):
	for j in range(0,len(grafos.vertex[i])):
		if grafos.vertex[i][j] == 1:
			G.add_edge(grafos.nodes[i],grafos.nodes[j])

for i in range(0,len(grafos.nodes)):
	G.node[listaNodes[i]]['color'] = mapa.getColor(i)
	nx.draw(G,pos,node_size = 1000,nodelist = grafos.nodes[i],node_color = color[mapa.getColor(i)])


plt.axis('off')
plt.show()
