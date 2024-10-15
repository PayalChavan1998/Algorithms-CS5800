# Payal Chavan
# CS 5800 Algorithms
# Summer 2024 (Seattle)
# HW #4
# Date: 06/14/2024

from simple_graph import Node
from graph_algorithms import dfs


# create a undirected graph with 2 Strongly Connected Components
def createGraph():
    graph = []

    graph.append( Node(0) )
    graph.append( Node(1) )
    graph.append( Node(2) )
    graph.append( Node(3) )
    graph.append( Node(4) )
    graph.append( Node(5) )
    graph.append( Node(6) )
    graph.append( Node(7) )
    graph.append( Node(8) )
    graph.append( Node(9) )

    graph[0].addUndirectedNeighbor( graph[2] )
    graph[0].addUndirectedNeighbor( graph[3] )
    graph[1].addUndirectedNeighbor( graph[2] )
    graph[2].addUndirectedNeighbor( graph[3] )
    graph[4].addUndirectedNeighbor( graph[5] )
    graph[4].addUndirectedNeighbor( graph[9] )
    graph[5].addUndirectedNeighbor( graph[6] )
    graph[6].addUndirectedNeighbor( graph[7] )
    graph[7].addUndirectedNeighbor( graph[8] )
    graph[7].addUndirectedNeighbor( graph[9] )
    graph[8].addUndirectedNeighbor( graph[9] )

    return graph


def main():
    graph = createGraph()
    print("\nDFS Results:")
    dfs( graph )


if __name__ == "__main__":
    main()
