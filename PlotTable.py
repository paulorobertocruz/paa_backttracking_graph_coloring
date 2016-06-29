import matplotlib.pyplot as plt
import networkx as nx
import grapth_star

G = nx.Graph()

nodes = ["a","b","c","d"]
G.add_nodes_from(nodes,color = "y")
pos = nx.random_layout(G)
color = nx.get_node_attributes(G,'color')

vertex = [[1,1,0,1],[1,1,1,1],[0,1,1,1],[1,1,1,1]]

for i in range(0,len(vertex)):
	for j in range(0,len(vertex[i])):
		if vertex[i][j] == 1:
			G.add_edge(nodes[i],nodes[j])

for i in range(0,len(nodes)):
	nx.draw(G,pos,node_size = 1000,nodelist = nodes[i],node_color = color[nodes[i]])

class Grafo:
    nodes = []
    def __init__(self):
        self.atualiza()

    def atualiza(self):
        self.n = len(self.nodes)
        self.m = 3
        self.x = [ 0 for _ in range(len(self.nodes))]

    def setNodes(self, nodes):
        self.nodes = nodes
        self.atualiza()

    def setVertex(self, vertex):
        self.vertex = vertex

    def setM(self, m):
        self.m = m

    def is_safe(self, k, c):
        for i in range(self.n):
            if self.vertex[k][i] == 1 and c == self.x[i]:
                return False
        return True


    def colora_node(self, k):
        for color in range(1, self.m+1):
            if self.is_safe(k,color):
                self.x[k] = color
                if k+1 < self.n:
                    self.colora_node(k+1)
                else:
                    #print(self.x)
                    return


plt.axis('off')
plt.show()