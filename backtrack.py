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

    def getCor(self,i):
        colors = {
            1:"red",
            2:"green",
            3:"blue",
            4:"white",
            5:"yellow",
        }
        return colors.get(i, "black")

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
        print(self.x)
        for color in range(1, self.m+1):
            if self.is_safe(k,color):
                self.x[k] = color
                if k+1 < self.n:
                    if self.colora_node(k+1):
                        return True
                    self.x[k] = 0
                else:
                    return True
        return False



nodes = ["a","b","c","d"]
vertex = [[1,1,0,1],[1,1,1,1],[0,1,1,1],[1,1,1,1]]

import grapth_star

a = Grafo()
a.setNodes(nodes)
a.setVertex(vertex)

if not a.colora_node(0):
    print("deu merda")
else:
    print(a.x)
