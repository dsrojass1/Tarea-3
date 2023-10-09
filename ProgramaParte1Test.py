import ProgramaParte1 as p1

def test_dijkstra_100():
    filenameGraph = "distances100.txt"
    graph = p1.create_graph(filenameGraph)
    filenameCostosMinimos = "distances100_costosminimos.txt"
    distancesMatrix = p1.create_graph(filenameCostosMinimos)
    assert p1.dijkstra(graph, 0) == distancesMatrix[0]

def test_bellman_ford_100():
    filenameGraph = "distances100.txt"
    graph = p1.create_graph(filenameGraph)
    filenameCostosMinimos = "distances100_costosminimos.txt"
    distancesMatrix = p1.create_graph(filenameCostosMinimos)
    assert p1.bellman_ford(graph, 0) == distancesMatrix[0]

def test_floyd_warshall_100():
    filenameGraph = "distances100.txt"
    graph = p1.create_graph(filenameGraph)
    filenameCostosMinimos = "distances100_costosminimos.txt"
    distancesMatrix = p1.create_graph(filenameCostosMinimos)
    assert p1.floyd_warshall(graph)[0] == distancesMatrix[0]
    
