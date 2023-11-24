from dijkstra import *
from pila import *
grafo_ejemplo = Grafo()
grafo_ejemplo.agregar_nodo('2 sur')
grafo_ejemplo.agregar_nodo('30 oriente')
grafo_ejemplo.agregar_nodo('11 oriente')
grafo_ejemplo.agregar_nodo('6 oriente')
grafo_ejemplo.agregar_nodo('16 sur')
grafo_ejemplo.agregar_nodo('2 norte')
grafo_ejemplo.agregar_nodo('26 sur')
grafo_ejemplo.agregar_nodo('26 1/2 sur')
grafo_ejemplo.agregar_nodo('6 poniente')
grafo_ejemplo.agregar_nodo('22 poniente')


grafo_ejemplo.agregar_arista('2 sur', '30 oriente', 15)
grafo_ejemplo.agregar_arista('2 sur', '16 sur', 20)
grafo_ejemplo.agregar_arista('30 oriente', '6 oriente', 6)
grafo_ejemplo.agregar_arista('30 oriente', '11 oriente', 8)
grafo_ejemplo.agregar_arista('6 oriente', '22 poniente', 10)
grafo_ejemplo.agregar_arista('11 oriente', '6 poniente', 7)
grafo_ejemplo.agregar_arista('16 sur', '2 norte', 5)
grafo_ejemplo.agregar_arista('16 sur', '26 sur', 3)
grafo_ejemplo.agregar_arista('16 sur', '6 poniente', 2)
grafo_ejemplo.agregar_arista('2 norte', '26 1/2 sur', 7)
grafo_ejemplo.agregar_arista('26 sur', '26 1/2 sur', 1)
grafo_ejemplo.agregar_arista('6 poniente', '22 poniente', 5)
grafo_ejemplo.agregar_arista('26 1/2 sur', '22 poniente', 4)



nodo_inicial = '2 sur'
nodo_destino = '22 poniente'

ruta_eficiente = dijkstra_unica_ruta(grafo_ejemplo, nodo_inicial, nodo_destino)

if ruta_eficiente:
    print(f"Camino con menos gasto de bencina desde {nodo_inicial} hasta {nodo_destino}:")
    for i in ruta_eficiente:
        print(i)
else:
    print(f"No hay ruta desde {nodo_inicial} hasta {nodo_destino}")
