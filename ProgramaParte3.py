
def create_graph(filename):
    graph = []
    with open(filename, 'r') as f:
        for line in f:
            graph.append(list(map(int, line.split())))  #Crear matriz de adyacencia.
    return graph

def DFS(graph): #Se usa DFS, sin embargo, solo se usará el atributo de color. 
    #Se utiliza un diccionario {#vertice : color}: Para representar a los vértices.
    V = {} 
    for i in range (0,len(graph)):
        V[i] = "blanco" 
    for vertex in V:
        if V[vertex] == "blanco":
            ciclo = DFSVisit(graph, V, vertex)
            if ciclo:
                return ciclo
    return ciclo
                           
def DFSVisit(graph, V, u): 
    ciclo = False
    V[u] = "gris" #"Colorea" de gris al vértice, lo que significa que lo visitamos
    for i in range(0,len(graph)):
        if graph[u][i]!= -1 and graph[u][i]!= 0: #Evita revisar en donde no existen caminos.
            if V[i] == "blanco":
                ciclo = DFSVisit(graph, V, i) #Llamado recursivo si el vertice no se ha visitado.
                if ciclo:
                    return True 
            elif V[i] == "gris": #Si el vertice que se quiere visitar ya es gris, significa que ya lo visitamos.
                                 #Entonces existe un arco que genera un ciclo.
                return True
    V[u] = "negro"
    return ciclo


filename = "distances5.txt" #Modificar esta linea para cambiar de archivo.
graph = create_graph(filename) #Matriz de adyacencia.
#print(graph)
ciclo = DFS(graph) #Retorna un Booleano
print("///\n")
if ciclo:
    print("-------------- El grafo cuenta con al menos un ciclo ---------------\n")
else:
    print("-------------- El grafo es acíclico ---------------\n")
print("///")