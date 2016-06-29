import sys
from backtrack import Grafo

if len(sys.argv) < 2:
    exit("ta faltando coisa")
m = 3
if len(sys.argv) == 3:
    m = int(sys.argv[2])

filename = sys.argv[1]

grafos = __import__("grafos."+filename, globals(), locals(), [filename, filename], 0)

mapa = Grafo()
mapa.setNodes(grafos.nodes)
mapa.setVertex(grafos.vertex)
mapa.setM(m)


if mapa.colora_node(0):
    print("tudo ok")
else:
    print("não deu solução")
