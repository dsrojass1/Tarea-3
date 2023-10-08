import numpy as np


def create_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = len(lines)
        graph = np.zeros((n, n))
        
        for i in range(n):
            values = lines[i].strip().split()
            for j in range(n):
                graph[i][j] = int(values[j])
                
        return graph

def dijkstra(graph, start):
    
    n = len(graph)
    INF = float('inf')

    visited = [False] * n
    distance = [INF] * n
    
    distance[start] = 0

    # Iterar sobre todos los vértices
    for _ in range(n):
        min_dist = INF
        
        # 'u' almacena el vértice con la distancia mínima
        u = -1

        # Encontrar el vértice no visitado con la distancia mínima
        for v in range(n):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                u = v

        visited[u] = True

        # Actualizar las distancias de los vértices adyacentes al vértice actual
        for v in range(n):
            if not visited[v] and graph[u][v] != -1 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

    return distance

def bellman_ford(graph, start):
    n = len(graph)
    INF = float('inf')
    distance = [INF] * n
    distance[start] = 0

    # Iterar n-1 veces (número máximo de aristas en un camino simple)
    for _ in range(n - 1): # Iterar sobre todos los vértices en el grafo
        for u in range(n): # Iterar sobre todos los vértices adyacentes a u
            for v in range(n):  # Actualizar la distancia si hay una arista de u a v y la distancia a través de u es menor que la distancia actual
                if graph[u][v] != -1 and distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    return distance

def floyd_warshall(graph):
    n = len(graph)
    distance = np.copy(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] != -1 and distance[k][j] != -1 and (distance[i][k] + distance[k][j] < distance[i][j] or distance[i][j] == -1):
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


filename = "distancesDisconnected.txt"
graph = create_graph(filename)

print('\n----------------------------------------- Dijkstra: \n')
for i in range(len(graph)):
    print(dijkstra(graph, i))

print('\n----------------------------------------- Bellman Ford: \n')
for i in range(len(graph)):
    print(bellman_ford(graph, i))

print('\n----------------------------------------- Floyd Warshall: \n')
print(floyd_warshall(graph))

