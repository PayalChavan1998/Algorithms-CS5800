# Bruce A. Maxwell
# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800 Algorithms
# Prim's Algorithm
# Date: 06/21/2024

from simple_heap import PQ
from simple_graph import Node

# function for comparing nodes in the PQ
def costcompare( a, b ):
    return a.cost() < b.cost()


# Implements Prim's algorithm for minimum spanning tree
# Takes in a list of type Node
# At the end of the algorithm...
#    all nodes will be visited (True)
#    all nodes will contain the cost of the edge connecting them to their MST parent
#    all nodes will indicate their parent node in the MST
def prim( graph ):

    # initialize the cost, parent, and visited fields

    # set the cost for the first Node to 0 (doesn't matter which node)
    graph[0].setCost(0)

    # make a PQ and add the first Node to the PQ
    pq = PQ( len(graph) * 2, costcompare )
    pq.add( graph[0] )

    # while the PQ is not empty
    while not pq.empty():
        # remove a node v from the PQ and set it as visited
        v = pq.remove()
        v.setVisited(True)

        # loop over each neighbor n of the node v
        for n_c in v.neighbors():
            n = n_c["node"]
            edge_cost = n_c["weight"]
        #   if n is not visited and its cost is greater than its edge weight
            if not n.visited() and n.cost() > edge_cost:
        #     set the cost of n to the edge weight
                n.setCost(edge_cost)
        #     set the parent of n to v
                n.setParent(v)
        #     add n to the PQ
                pq.add(n)


# main test function
def main():

    # run the first example from 5.1 in Dasgupta
    print("Graph 1")
    graph = []
    for i in range(6):
        graph.append( Node( i ) )

    graph[0].addUndirectedNeighbor( graph[1], 4 )
    graph[0].addUndirectedNeighbor( graph[2], 1 )
    graph[0].addUndirectedNeighbor( graph[3], 3 )

    graph[1].addUndirectedNeighbor( graph[2], 4 )
    graph[1].addUndirectedNeighbor( graph[3], 4 )

    graph[2].addUndirectedNeighbor( graph[3], 2 )
    graph[2].addUndirectedNeighbor( graph[5], 4 )
    
    graph[3].addUndirectedNeighbor( graph[5], 6 )
    
    graph[4].addUndirectedNeighbor( graph[5], 5 )

    prim(graph)
    
    print("Prim's Results 1")
    sum = 0
    for node in graph:
        print(node)
        sum += node.cost()
    print("Total cost of graph 1: %d" % (sum) )
   
    # run a graph, Figure 5.1 from Dasgupta
    print("\nGraph 2")
    graph = []
    for i in range(6):
        graph.append( Node( i ) )

    graph[0].addUndirectedNeighbor( graph[1], 5 )
    graph[0].addUndirectedNeighbor( graph[2], 6 )
    graph[0].addUndirectedNeighbor( graph[3], 4 )

    graph[1].addUndirectedNeighbor( graph[2], 1 )
    graph[1].addUndirectedNeighbor( graph[3], 2 )

    graph[2].addUndirectedNeighbor( graph[3], 2 )
    graph[2].addUndirectedNeighbor( graph[4], 5 )
    graph[2].addUndirectedNeighbor( graph[5], 3 )
    
    graph[3].addUndirectedNeighbor( graph[5], 4 )
    
    graph[4].addUndirectedNeighbor( graph[5], 4 )

    prim(graph)
    
    print("\nPrim's Results 2")
    sum = 0
    for node in graph:
        print(node)
        sum += node.cost()

    print("Total cost of graph 2: %d" % (sum) )
        
    return

if __name__ == "__main__":
    main()