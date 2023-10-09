import time


def create_graph(filename):
    graph = []
    with open(filename, 'r') as f:
        for line in f:
            graph.append(list(map(int, line.split())))  
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
    distance = graph.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] != -1 and distance[k][j] != -1 and (distance[i][k] + distance[k][j] < distance[i][j] or distance[i][j] == -1):
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

if __name__ == '__main__':
    filename = "distances100.txt"
    graph = create_graph(filename)

    print('\n----------------------------------------- Dijkstra: \n')
    start = time.time()
    distancesMatrixDijsktra = []
    for i in range(len(graph)):
        distancesMatrixDijsktra.append(dijkstra(graph, i))
    end = time.time()
    print(distancesMatrixDijsktra)
    print('\nTiempo de ejecución: ', end - start)

    print('\n----------------------------------------- Bellman Ford: \n')
    start = time.time()
    distancesMatrixBellmanFord = []
    for i in range(len(graph)):
        distancesMatrixBellmanFord.append(bellman_ford(graph, i))
    end = time.time()
    print(distancesMatrixBellmanFord)
    print('\nTiempo de ejecución: ', end - start)

    print('\n----------------------------------------- Floyd Warshall: \n')
    start = time.time()
    distancesMatrixFloydWarshall = floyd_warshall(graph)
    end = time.time()
    print(distancesMatrixFloydWarshall)
    print('\nTiempo de ejecución: ', end - start)

