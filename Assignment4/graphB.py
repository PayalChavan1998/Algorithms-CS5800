# Payal Chavan
# CS 5800 Algorithms
# Summer 2024 (Seattle)
# HW #4
# Date: 06/14/2024

from simple_graph import Node
from graph_algorithms import dijkstra


# create directed graph
def createGraph():
    graph = []

    graph.append( Node(0, 10, 40) )
    graph.append( Node(1, 20, 60) )
    graph.append( Node(2, 50, 50) )
    graph.append( Node(3, 60, 80) )
    graph.append( Node(4, 80, 100) )
    graph.append( Node(5, 90, 70) )
    graph.append( Node(6, 110, 40) )
    graph.append( Node(7, 120, 120) )

    graph[0].addDirectedNeighbor( graph[1] )
    graph[1].addDirectedNeighbor( graph[2] )
    graph[2].addDirectedNeighbor( graph[3] )
    graph[2].addDirectedNeighbor( graph[5] )
    graph[3].addDirectedNeighbor( graph[4] )
    graph[3].addDirectedNeighbor( graph[6] )
    graph[4].addDirectedNeighbor( graph[5] )
    graph[5].addDirectedNeighbor( graph[6] )
    graph[6].addDirectedNeighbor( graph[7] )
    graph[5].addDirectedNeighbor( graph[7] )

    return graph


def main():
    graph = createGraph()
    dijkstra( graph, graph[0] )
    # print the results
    print("\nDijkstra's Results:")
    for node in graph:
        print(node)

if __name__ == "__main__":
    main()
