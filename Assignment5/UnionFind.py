# Bruce A. Maxwell
# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Union-Find implementation
# Date: 06/21/2024

# Simple Node class for a Union-Find data structure
class UFNode:

    def __init__(self, id):
        self._parent = None
        self._rank = 0
        self._id = id

    def id(self):
        return self._id

    def setParent(self, p):
        self._parent = p

    def parent(self):
        return self._parent

    def rank(self):
        return self._rank

    def setRank(self, r):
        self._rank = r

    def __str__(self):
        return "(%d -> %d)" % (self._id, findSimple( self )._id )

# takes in two Nodes and merges them into the same class
# makes the root of one node be the parent of the root of the other
# Chooses the root with higher rank to be the new root
# returns nothing
def union( a, b ):
    # algorithm here
    root_a = findSimple(a)
    root_b = findSimple(b)

    if root_a == root_b:
      return
    

    if root_a.rank() < root_b.rank():
        root_a.setParent(root_b)
    elif root_a.rank() > root_b.rank():
        root_b.setParent(root_a)
    else:
        root_b.setParent(root_a)
        root_a.setRank(root_a.rank() + 1)

# find algorithm that does not implement path compression
# follows the parent pointers to the root with a None parent
# returns the root
def findSimple( a ):
    while a.parent() is not None:
        a = a.parent()
    return a
                               

# find algorithm that implements path compression
# follows parent pointers using recursion
# resets the parent of each node along the way to the parent node
# returns the parent
def find( a ):
    if a.parent() is not None:
        a.setParent(find(a.parent()))
    return a
   


# test function for union-find
def main():

    graph = []
    
    # make some nodes in the graph
    for i in range(10):
        graph.append( UFNode(i) )

    print("Initial groups")
    for n in graph:
        print(n)

    union( graph[0], graph[8] )

    union( graph[3], graph[4] )

    print("\nSecond")
    for n in graph:
        print(n)

    union( graph[3], graph[5] )

    union( graph[8], graph[4] )

    union( graph[2], graph[7] )

    union( graph[2], graph[9] )

    print("\nThird")
    for n in graph:
        print(n)

    union( graph[1], graph[9] )

    union( graph[8], graph[6] )

    print("\nFourth")
    for n in graph:
        print(n)

    union( graph[9], graph[3] )

    print("unions done")

    print("\nFinal")
    for n in graph:
        print(n)
    


if __name__ == "__main__":
    main()


'''
Output:

Initial groups
(0 -> 0)
(1 -> 1)
(2 -> 2)
(3 -> 3)
(4 -> 4)
(5 -> 5)
(6 -> 6)
(7 -> 7)
(8 -> 8)
(9 -> 9)

Second
(0 -> 0)
(1 -> 1)
(2 -> 2)
(3 -> 3)
(4 -> 3)
(5 -> 5)
(6 -> 6)
(7 -> 7)
(8 -> 0)
(9 -> 9)

Third
(0 -> 0)
(1 -> 1)
(2 -> 2)
(3 -> 3)
(4 -> 0)
(5 -> 3)
(6 -> 6)
(7 -> 2)
(8 -> 0)
(9 -> 2)

Fourth
(0 -> 0)
(1 -> 1)
(2 -> 2)
(3 -> 3)
(4 -> 0)
(5 -> 3)
(6 -> 0)
(7 -> 2)
(8 -> 0)
(9 -> 1)
unions done

Final
(0 -> 0)
(1 -> 1)
(2 -> 2)
(3 -> 3)
(4 -> 0)
(5 -> 3)
(6 -> 0)
(7 -> 2)
(8 -> 0)
(9 -> 3)

'''