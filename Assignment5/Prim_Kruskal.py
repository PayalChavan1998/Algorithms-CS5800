# Bruce A. Maxwell
# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800 Algorithms
# Prim's and Kruskal's Algorithm
# Date: 06/21/2024


from simple_graph import Node
from prims import prim
from kruskal import kruskal


def run_prims(graph):
    prim(graph)
    
    print("\nPrim's Results")
    sum = 0
    for node in graph:
        print(node)
        sum += node.cost()

    print("Total cost of graph: %d" % (sum) )


def run_kruskal(graph):

    edges = kruskal( graph )

    print("Kruskal's Results")

    sum = 0
    for e in edges:
        sum += e.weight()
        print("edge from %d to %d with weight %d" % (e.A().id(), e.B().id(), e.weight() ))

    print("Total cost of graph: %d" % (sum) )


def create_graph():
    graph = []
    for i in range(8):
        graph.append( Node( i ) )

    graph[0].addUndirectedNeighbor( graph[1], 1 )
    graph[0].addUndirectedNeighbor( graph[2], 2 )
    graph[0].addUndirectedNeighbor( graph[3], 4 )
    graph[0].addUndirectedNeighbor( graph[4], 8 )
    graph[0].addUndirectedNeighbor( graph[5], 4 )
    graph[0].addUndirectedNeighbor( graph[6], 2 )
    graph[0].addUndirectedNeighbor( graph[7], 6 )
    graph[1].addUndirectedNeighbor( graph[2], 2 )
    graph[1].addUndirectedNeighbor( graph[7], 1 )
    graph[2].addUndirectedNeighbor( graph[3], 5 )
    graph[2].addUndirectedNeighbor( graph[6], 8 )
    graph[3].addUndirectedNeighbor( graph[4], 8 )
    graph[3].addUndirectedNeighbor( graph[5], 2 )
    graph[4].addUndirectedNeighbor( graph[5], 3 )
    graph[5].addUndirectedNeighbor( graph[6], 9 )
    graph[6].addUndirectedNeighbor( graph[7], 7 )

    return graph

if __name__ == "__main__":
    graph = create_graph()
    run_prims(graph)
    print("-" * 25)
    run_kruskal(graph)
