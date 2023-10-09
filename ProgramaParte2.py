 
import numpy as np

x = [[-1,-1,-1,1,-1,-1,-1],
     [-1,-1,-1,-1,-1, 1,1],
     [-1,-1,-1,1,-1,-1,-1],
     [ 1,-1,1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1,1],
     [-1,1,-1,-1,-1,-1,-1],
     [-1,1,-1,-1,1,-1,-1]]


def bfs (matriz,vertice,visitados):
    cola = []
    cola.append(vertice)
    visitados[vertice] = True
    res = []
    res.append(vertice)

   
    

    while cola  != []:

        nuevovertice  = cola.pop(0)
  
        for cerca in range(len(matriz[nuevovertice])):
          
            if matriz[nuevovertice][cerca] == 1  and visitados[cerca] == False:
                cola.append(cerca)
                res.append(cerca)
                visitados[cerca] = True
                

 
    return res,visitados



    



def componentes_conectados(grafo):
    resultado = []
    visitados = {}
    for vertice in range(len(grafo)):
        visitados[vertice] = False
    
    for vertice in range(len(grafo)):
        if not visitados[vertice]:
           
            r,f = bfs(grafo,vertice,visitados)
            resultado.append(r)
            visitados = f
    return resultado



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
                    

archivo = "ejemploParte2.txt"
graph = create_graph(archivo)

resultado = componentes_conectados(graph)
contador = 1
for i in resultado:
   
    print("---",contador , "Componente conectado --- ")
    print("\n")
    print(i)
    print("\n")
    contador+=1
    
            