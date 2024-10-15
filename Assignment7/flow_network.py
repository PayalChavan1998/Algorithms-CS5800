# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Assignment 7
# Coding Que1: Part_A & Part_B - Linear Programming for Maximum Flow Problem 
# Date: 07/20/2024




'''
Code up the flow network for given graph as a linear program and use the scipy linprog solver to identify the flow on each edge.
following graph represent the flow from node i to node j. The value of the edge represents the capacity of the edge.
graph = [[0, 10, 0, 10, 0, 0],
        [0, 0, 3, 2, 2, 5],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0]]
'''

# Import necesarry libraries
import numpy as np
from scipy.optimize import linprog
from scipy.optimize import OptimizeResult
import networkx as nx
import matplotlib.pyplot as plt

# Example graph with 6 nodes and 9 edges
# Nodes: 0 (source), 1, 2, 3, 4, 5 (sink)
# Edges: (0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (1, 5) ,(2, 5), (3, 4), (4, 5)
# Capacities: [10, 10, 3, 2, 5, 5, 5, 3, 5]

num_nodes = 6

# Edge list and capacities
edges_A = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (1, 5) ,(2, 5), (3, 4), (4, 5)]
capacities_A = [10, 10, 3, 2, 2, 5, 5, 3, 5]

# Edge list and capacities
edges_B = [(0, 1), (0, 3), (1, 2), (1, 4), (1, 5) ,(2, 5), (3, 4), (4, 5)]
capacities_B = [10, 10, 3, 2, 5, 5, 4, 6]

# Define edge_capacity for both part_A and part_B of the question
def edge_capacity(part_B):
    if part_B:
        edges = edges_B
        capacities = capacities_B
    else:
        edges = edges_A
        capacities = capacities_A

    return edges, capacities


# Define setup function 
def setup(part_B):
    edges, capacities = edge_capacity(part_B)

    # Objective function: maximize the flow (negative for linprog minimization)
    # Objective function: minimize the negative flow (maximize flow)
    # The objective function c is set to zero 
    # since we are only interested in the constraints and bounds to find the maximum flow.
    c = np.zeros(len(edges))

    # Set the coefficients for the edges we want to maximize
    # Assuming we want to maximize the flow from source (any) to sink (5)
    for i, (u, v) in enumerate(edges):
        if v == 5:  # Sink node
            c[i] = -1

    # Constraints: flow conservation at each node except source and sink
    incidence_matrix = np.zeros((num_nodes, len(edges)))    # A_eq

    # Flow conservation constraints
    for i, (u, v) in enumerate(edges):
        incidence_matrix[u, i] = 1
        incidence_matrix[v, i] = -1

    # Source and sink constraints
    # Source is node 0, sink is node 5
    supply_demand = np.zeros(num_nodes)         # b_eq
    supply_demand[0] = 14 if part_B else 13     # Source
    supply_demand[5] = -14 if part_B else -13   # Sink

    # Bounds for each edge (0 <= flow <= capacity)
    bounds = [(0, capacity) for capacity in capacities]

    # Constraints: Ax = b
    return c, incidence_matrix, supply_demand, bounds 


# Solve the linear programming problem
def main(part_B=False):
    c, incidence_matrix, supply_demand, bounds = setup(part_B)
    result: OptimizeResult = linprog(c,
                                     A_eq=incidence_matrix, 
                                     b_eq=supply_demand,
                                     bounds=bounds,
                                     method='highs'
                                    )

    if result.success:
        print("Optimal flow:", -result.fun)
        print("Flow values on edges:", result.x)
        plot_graph(result, part_B)
    else:
        print("The problem is infeasible or unbounded.")


# Draw the graph showing optimal path
def plot_graph(result: OptimizeResult, part_B=False):
    edges, capacities = edge_capacity(part_B)

    # Visualization
    G = nx.DiGraph()
    for i, (u, v) in enumerate(edges):
        G.add_edge(u, v, capacity=capacities[i], flow=result.x[i])

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f'{G[u][v]["flow"]}/{G[u][v]["capacity"]}' for u, v in G.edges}

    # fig = plt.figure(num='MyFigureName', figsize=(8, 6), dpi=100)
    que_number = "Part B" if part_B else "Part A"
    figure_title = "Maximum Flow in the Graph: " + que_number
    plt.figure(num=figure_title, figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=14, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=14)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=2, alpha=0.6, edge_color='black')
    plt.show()
    # plt.savefig('flow_network.png')


if __name__ == "__main__":
    print("Part - A")
    main(part_B=False)
    print("\nPart - B")
    main(part_B=True)
