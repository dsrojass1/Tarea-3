# Tarea-3
### Integrantes:
- David Santiago Gómez Martínez
- David Samuel Rojas Sanchez
- Josue Vega Valbuena

## Parte 1 (ProgramaParte1.py):
Este programa implementa los algoritmos de ruta mínima: Dijkstra, Bellman Ford y Floyd Warshall. El programa lee un archivo de texto que representa un grafo ponderado y muestra las rutas mínimas desde cada vértice hasta todos los demás.

**Para leer un archivo, asegurarse que cumpla con el formato de entrada y que esté dentro de la carpeta en donde se encuentra el programa. Luego modificar la línea de código 70 asignando a la variable filename el nombre del archivo que represente el grafo:** 

Ejemplo:

```
filename = "distances100.txt"
```

**IMPORTANTE: Con el programa 'ProgramaParte1Test.py' es posible probar los algoritmos con el ejemplo 'distances100_costosminimos'.**

**IMPORTANTE: Se adjunta en el repositorio el documento 'PARTE 1 COMPARACION TIEMPOS EJECUCION' en donde se ejecutar cada uno de los algoritmos con las matrices adjuntas y se comparan los tiempos de ejecución.**

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

[[0, 2, 4, 1], [-1, 0, 4, -1], [-1, -1, 0, 2], [-1, -1, -1, 0]]

----------------------------------------- Bellman Ford:

[[0, 2, 4, 1], [-1, 0, 4, -1], [-1, -1, 0, 2], [-1, -1, -1, 0]]

----------------------------------------- Floyd Warshall:

[[0, 2, 4, 1], [-1, 0, 4, -1], [-1, -1, 0, 2], [-1, -1, -1, 0]]
```


## Parte 2 (ProgramaParte2.py):

En este programa se implementa una solucion al problema de hallar componentes conectados en un grafo que no es dirigido.

**Para leer un archivo, asegurarse que cumpla con el formato de entrada y que esté dentro de la carpeta en donde se encuentra el programa. Luego modificar la línea de código 74 asignando a la variable "archivo" el nombre del archivo que represente el grafo:** 


## Formato del archivo de entrada 
El programa recibe como input un archivo de texto en el cual se encuentra el grafo separado por tabs (tabulaciones) 
Ejemplo : 
```
-1	-1	-1	1	-1	-1	-1
-1	-1	-1	-1	-1	1	-1
-1	-1	-1	1	-1	-1	-1
1	-1	1	-1	-1	-1	-1
-1	-1	-1	-1	-1	-1	1
-1	1	-1	-1	-1	-1	-1
-1	-1	-1	-1	1	-1	-1
```
Cada numero esta separado por una tabulacion y para cada fila existe un "enter".

Los indices en la matriz pueden tomar dos valores: 1 si existe una relacion entre los vertices o -1 si no existe esta relacion.
La matriz es simetrica debido a que el grafo no es dirigido, por lo que la relacion del vertice 0 al 1, debe existir al mismo tiempo que la relacion de 1 a 0.

## Formato de salida 

Como resultado tenemos los componentes conectados o especificamente los vertices que se conectan entre si.

se presenta de la siguiente forma:

Ejemplo: 

```

--- 1 Componente conectado ---


[1, 5]


--- 2 Componente conectado ---


[4, 6]

```


## Parte 3 (ProgramaParte3.py):
Este programa implementa una variante del algoritmo DFS, lo anterior con el objetivo de verificar si un grafo dirigido dado tiene o no ciclos. El programa lee un archivo de texto que representa un grafo ponderado y verifica si existen ciclos en el mismo.

**Para leer un archivo, asegurarse que cumpla con el formato de entrada y que esté dentro de la carpeta en donde se encuentra el programa. Luego modificar la línea de código 37 asignando a la variable filename el nombre del archivo que represente el grafo:** 

Ejemplo:

```
filename = "distances5.txt"
```

**IMPORTANTE: El archivo por defecto es "distances5.txt", sin embargo, es posible probar otros dos casos con los archivos "distances5NC.txt" y "distances5NC2.txt".**

### Formato del Archivo de Entrada
El programa espera un archivo de texto que represente un grafo ponderado. Cada línea del archivo debe contener los pesos de las aristas desde un vértice hasta todos los demás, separados por espacios. Un valor de -1 indica que no hay conexión directa entre los vértices. Adicionalmente, el valor 0 indica que no existe un arco que conecte un vertice con el mismo directamente. 

Ejemplo:

```
0	90	80	-1	-1
15	0	69	48	-1
91	-1	0	12	39
78	-1	-1	0	36
26	12	39	33	0
```

En este ejemplo, el vértice 0 está conectado con el vértice 1 con un peso de 90 y, a su vez, el vértice 1 está conectado al vértice 0 con un peso de 15. En este caso el grafo posee al menos un ciclo.

### Salida
El programa imprimirá un mensaje que indica si el grafo posee al menos un ciclo o si, por el contrario, es acíclico. (La función DFS retorna un booleano que indica si existen o no ciclos en el grafo)

Ejemplo:

```
-------------- El grafo cuenta con al menos un ciclo ---------------
```
