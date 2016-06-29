import sys
from backtrack import Grafo

if len(sys.argv) < 2:
    exit("ta faltando coisa")

filename = sys.argv[1]

grafos = __import__("grafos."+filename, globals(), locals(), [filename, filename], 0)

mapa = Grafo()
mapa.setNodes(grafos.nodes)
mapa.setVertex(grafos.vertex)

if mapa.colora_node(0):
    print("tudo ok")
else:
    print("não deu solução")
