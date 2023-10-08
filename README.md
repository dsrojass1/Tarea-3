# Tarea-3
### Integrantes:
- David Santiago Gómez Martínez
- David Samuel Rojas Sanchez
- Josue Vega Valbuena

## Parte 1 (ProgramaParte1.py):
Este programa implementa los algoritmos de ruta mínima: Dijkstra, Bellman Ford y Floyd Warshall. El programa lee un archivo de texto que representa un grafo ponderado y muestra las rutas mínimas desde cada vértice hasta todos los demás.

**Para leer un archivo, asegurarse que cumpla con el formato de entrada y que esté dentro de la carpeta en donde se encuentra el programa. Luego modificar la línea de código 77 asignando a la variable filename el nombre del archivo que represente el grafo:** 

Ejemplo:

```
filename = "distances100.txt"
```

### Formato del Archivo de Entrada
El programa espera un archivo de texto que represente un grafo ponderado. Cada línea del archivo debe contener los pesos de las aristas desde un vértice hasta todos los demás, separados por espacios. Un valor de -1 indica que no hay conexión directa entre los vértices.

Ejemplo:

```
0 2 -1 1
-1 0 4 -1
-1 -1 0 2
-1 -1 -1 0
```

En este ejemplo, el vértice 1 está conectado con el vértice 2 con un peso de 2 y con el vértice 4 con un peso de 1.

### Salida
El programa imprimirá las distancias mínimas desde cada vértice hasta todos los demás utilizando los algoritmos de Dijkstra, Bellman Ford y Floyd Warshall.

Ejemplo:

```
----------------------------------------- Dijkstra:

[0, 2, 4, 1]
[-1, 0, 4, -1]
[-1, -1, 0, 2]
[-1, -1, -1, 0]

----------------------------------------- Bellman Ford:

[0, 2, 4, 1]
[-1, 0, 4, -1]
[-1, -1, 0, 2]
[-1, -1, -1, 0]

----------------------------------------- Floyd Warshall:

[[ 0.  2.  4.  1.]
 [-1.  0.  4. -1.]
 [-1. -1.  0.  2.]
 [-1. -1. -1.  0.]]
```