# Bruce A. Maxwell
# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800 Algorithms
# Kruskal's Algorithm Template
# Date: 06/21/2024


import UnionFind as uf
from simple_graph import Node


# Simple Edge class
# immutable once created
class Edge:

    def __init__(self, nodeA, nodeB, weight):
        self._a = nodeA
        self._b = nodeB
        self._weight = weight

    def weight(self):
        return self._weight

    def A(self):
        return self._a

    def B(self):
        return self._b

    def __str__(self):
        return "%d to %d weight %d" % (self._a.id(), self._b.id(), self._weight )


# Takes graph, which is a list of type Node
# Returns a list of type Edge that form the minimum spanning tree
def kruskal( graph ):

    # initialize a list for UFNode type, to hold all nodes
    uf_nodes = []

    # initialization of Union-Find sets
    # create a UFNode for each node in the graph, make the id be the index
    for node in graph:
        uf_nodes.append(uf.UFNode(node.id()) )

    # sort uf_nodes by id
    uf_nodes.sort(key=lambda x: x.id())

    # initialize a list of Edge type, to hold all edges
    edges = []

    # initialize the list of all edges
    # create a list of the unique edges in G
    # you can use the ids to avoid adding duplicates
    # for example, don't add 2->1 if 1->2 is already in the list
    for node in graph:
        for n_c in node.neighbors():
            neighbor = n_c["node"]
            edge_cost = n_c["weight"]
            uf_node_A = uf_nodes[node.id()]
            uf_node_B = uf_nodes[neighbor.id()]

            if node.id() < neighbor.id():
                edges.append( Edge( uf_node_A, uf_node_B, edge_cost ) )

    # Initialize the minimum spanning tree X to the empty set
    X = []

    # sort the edges, use Edge.weight as the key
    edges.sort(key=lambda x: x.weight())

    # for each edge, if the two edges are not part of the same set, add to X and call union
    for edge in edges:
        # print(edge)
        nodeA = edge.A()
        nodeB = edge.B()
        # uf.find( nodeA )
        if uf.findSimple( nodeA ) != uf.findSimple( nodeB ):
            X.append( edge )
            uf.union( nodeA, nodeB )

    return X


# Main test function
# Tests two example graphs
# Create at least one other test graph with at least 8 nodes and 16 edges
def main():

    # run the first example from 5.1 in Dasgupta
    print("Graph 1")
    graph = []
    for i in range(6):
        graph.append( Node( i ) )

    # A -> B 4
    graph[0].addUndirectedNeighbor( graph[1], 4 )
    # A -> C 1
    graph[0].addUndirectedNeighbor( graph[2], 1 )
    # A -> D 3
    graph[0].addUndirectedNeighbor( graph[3], 3 )
    # B -> C 4
    graph[1].addUndirectedNeighbor( graph[2], 4 )
    # B -> D 4
    graph[1].addUndirectedNeighbor( graph[3], 4 )
    # C -> D 2
    graph[2].addUndirectedNeighbor( graph[3], 2 )
    # C -> F 4
    graph[2].addUndirectedNeighbor( graph[5], 4 )
    # D -> F 6
    graph[3].addUndirectedNeighbor( graph[5], 6 )
    # E -> F 5
    graph[4].addUndirectedNeighbor( graph[5], 5 )

    edges = kruskal( graph )

    sum = 0
    for e in edges:
        sum += e.weight()
        print("edge from %d to %d with weight %d" % (e.A().id(), e.B().id(), e.weight() ))

    # should be 16
    print("Total cost of graph 1: %d" % (sum) )

    # run a second graph, Figure 5.1 from Dasgupta
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
    
    edges = kruskal( graph )

    sum = 0
    for e in edges:
        sum += e.weight()
        print("edge from %d to %d with weight %d" % (e.A().id(), e.B().id(), e.weight() ))

    # should be 14
    print("Total cost of graph 1: %d" % (sum) )



# call main if this file is executed
if __name__ == "__main__":
    main()
