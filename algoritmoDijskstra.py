# valor de infinito (sys.maxsize) na inicialização das distâncias
import sys

def calcularDijkstra(grafo, origem):

    # inicialização das distâncias com o valor infinito; a origem é zero
    distancias = {v: sys.maxsize for v in grafo}
    distancias[origem] = 0

    # conjunto de vértices visitados
    visitados = set()

    while visitados != set(distancias):
        # encontra o vértice não visitado com menor distância atual
        vertice_atual = None
        menor_distancia = sys.maxsize

        for v in grafo:
            if v not in visitados and distancias[v] < menor_distancia:
                vertice_atual = v
                menor_distancia = distancias[v]

        # marca o vértice atual como visitado
        visitados.add(vertice_atual)

        # atualiza as distâncias dos vértices vizinhos
        for vizinho, peso in grafo[vertice_atual].items():
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[vertice_atual] + peso

    # retorna as distâncias mais curtas a partir da origem
    return distancias

# definição do grafo com as conexões e distâncias entre os nós
grafo = {
    "A": {"B": 2, "C": 1},
    "B": {"A": 2, "D": 1},
    "C": {"A": 1, "E": 4},
    "D": {"B": 1, "C": 3, "F": 2},
    "E": {"C": 4, "F": 2},
    "F": {"D": 2, "E": 2},
}

origem = "A"

caminhoMaisCurto = calcularDijkstra(grafo, origem)

print("Algoritmo de Dijkstra")
print("Origem:", origem, "\n")

for destino, distancia in caminhoMaisCurto.items():
    print(f"Caminho mais curto de {origem} para {destino}: {distancia}")