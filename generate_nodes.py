import random
import sys

if len(sys.argv) < 3:
    print("argumentos:python generate_nodes.py numero_de_nos numero_maximo_de_conexões")
    exit()

quantidade = int(sys.argv[1])
max_conections = int(sys.argv[2])

def get_number_conection(max_conections):
    p = random.randint(1,10)
    if p > 7:
        # 30% mais da metade conexões
        p = random.randint(1,10)
        min_conections = max_conections/2
        mid_conections = int(max_conections - min_conections / 2)
        if p >= 4:
            number = random.randint(int(min_conections), int(mid_conections))
        else:
            number = random.randint(mid_conections, int(max_conections))
    else:
        # 70% menos da metade conexões
        p = random.randint(1,10)
        max_conections = max_conections/2
        if p > 6:
            number = random.randint(int(max_conections/2), int(max_conections))
        else:
            number = random.randint(1, int(max_conections/2))
    return number

def conecta():
    if random.randint(1,10) > 8:
        return True
    else:
        return False

nodes = [get_number_conection(max_conections) for _ in range(quantidade)]
vertex = [[0 for _ in range(quantidade)] for _ in range(quantidade)]

#self conecta
for n in range(len(nodes)):
    vertex[n][n] = 1


def popula_conection(d = 0):
    for n in range(len(nodes)):
        for j in range(len(nodes)):
            if n != j and nodes[n]-1 > 0 and vertex[n][j] != 1:
                if conecta():
                    nodes[n] = nodes[n] - 1
                    vertex[n][j] = 1
    if max(nodes) > 0:
        if d >10:
            return
        popula_conection(d+1)

for n in range(len(nodes)):
    nodes[n] = n


filename = "grafos/mapa_" + str(quantidade) + "_" + str(max_conections) + ".py"
arquivo = open(filename,"w")
arquivo.write("nodes = " + str(nodes) + "\n")

popula_conection()

arquivo.write("vertex = " + str(vertex) + "\n")

arquivo.close()
