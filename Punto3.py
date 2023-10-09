import time


def create_graph(filename):
    graph = []
    with open(filename, 'r') as f:
        for line in f:
            graph.append(list(map(int, line.split())))  
    return graph

def DFS(graph):
    V = {}
    for i in range (0,len(graph)-1):
        V[i] = {"color" : "blanco"}
    for vertex in V:
        if V[vertex]["color"] == "blanco":
            ciclo = DFSVisit(graph, V, vertex)
            if ciclo:
                return ciclo
    return ciclo
                           
def DFSVisit(graph, V, u):
    ciclo = False
    V[u]["color"] = "gris"
    for i in range(1,len(graph)-1):
        if graph[u][i]!= -1 and graph[u][i]!= 0:
            if V[i]["color"] == "blanco":
                ciclo = DFSVisit(graph, V, i)
            elif V[i]["color"] == "gris":
                return True
    V[u]["color"] = "negro"
    return ciclo


        

filename = "distances5NC.txt"
graph = create_graph(filename)
print(graph)
ciclo = DFS(graph)
print(ciclo)
