# Payal Chavan
# Summer 2024 
# Algorithms CS 5800
# Synthesis3 - Shortest Path on a DAG
# Date: 08/09/2024


from collections import defaultdict, deque

def topological_sort(V, adj):
    # Calculate in-degrees for each vertex
    in_degree = [0] * V
    for u in range(V):
        for v, _ in adj[u]:
            in_degree[v] += 1
    
    # Initialize a queue with source vertices (in-degree 0)
    queue = deque([u for u in range(V) if in_degree[u] == 0])
    topo_order = []

    # Perform topological sorting
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return topo_order

def shortest_path_dag(V, edges, S, T):
    # Create an adjacency list representation of the graph
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))

    # Get the topological order of vertices
    topo_order = topological_sort(V, adj)
    
    # Initialize distances and predecessors
    dist = [float('inf')] * V
    # set distance to 0 for Source vertex/node
    dist[S] = 0
    # predecessor = to get the Source to Target path
    pred = [-1] * V


    # Relax edges based on topological order
    for u in topo_order:
        if dist[u] != float('inf'):
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u
    
    # Calculate the path from source to target
    path = []
    if dist[T] != float('inf'):
        current = T
        while current != -1:
            path.append(current)
            current = pred[current]
        path.reverse()
    
    return path, dist[T]

# Execute the main function to test the code.
if __name__ == "__main__":
    V = 6
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (1, 3, 6),
        (1, 2, 2),
        (2, 4, 4),
        (2, 5, 2),
        (2, 3, 7),
        (3, 4, -1),
        (4, 5, -2)
    ]
    S = 0
    T = 5

    path, distance = shortest_path_dag(V, edges, S, T)
    print(f"Shortest Path from {S} to {T}: {' -> '.join(map(str, path))}")
    print(f"Shortest Distance from {S} to {T}: {distance}")





'''
Output:
Shortest Path from 0 to 5: 0 -> 2 -> 5
Shortest Distance from 0 to 5: 5
'''