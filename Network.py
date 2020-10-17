import networkx as nx
import matplotlib.pyplot as plt
import metro

g = nx.Graph()

i = 1
for linea in metro.lineas:
    print( "linea" , i )
    for idx in range(len(linea) - 1):
        g.add_edge(linea[idx], linea[idx + 1])
        print( "    " , linea[idx], linea[idx - 1] )
    i = i + 1

nx.draw_spring(g, with_labels=True)
plt.show()