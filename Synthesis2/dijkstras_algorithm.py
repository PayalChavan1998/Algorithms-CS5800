# CS 5800 Algorithms
# Summer 2024
# Payal Chavan
# Synthesis Assignment -2
# Topic: Dijkstra's Algorithm
# Date: 07/10/2024



'''
There are n cities connected by some number of flights.
You are given an array flights
    where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
    You are also given three integers src, dest, and k, return the cheapest price from src to dest with at most k stops.
If there is no such route, return -1.
'''

# import necessary libraries
import heapq
from collections import defaultdict

# Function to find the cheapest price flight from source to destination with required steps
def findCheapestPrice(flights: list[list[int]], src: int, dest: int, k: int) -> int:

    # Make adjacency list of flights
    adj_list = defaultdict(list)
    for u, v, w in flights:
        adj_list[u].append((v,w))

    # initialize minimim priority queue with start node, cost 0 and step -1 (as this is source node)
    pri_queue = [ (0, -1, src) ] # weight, steps, node

    while pri_queue:
        cost, steps, node = heapq.heappop(pri_queue)

        # if steps is more than max allowed step we skip this node
        if steps > k:
            continue
        
        # if current node is destination then return cost
        if node == dest:
            return cost

        # for all neighboring nodes of current node, calculate distance and put in minimum priority queue
        for neighb, weight in adj_list[node]:
            heapq.heappush(pri_queue, (cost + weight, steps + 1, neighb))

    return -1


# Driver program to test the code
if __name__ == '__main__':
    flights = [
        ['A', 'B', 100],
        ['A', 'G', 250],
        ['B', 'H', 350],
        ['H', 'F', 500],
        ['G', 'F', 150],
        ['F', 'I', 90],
        ['I', 'C', 900],
        ['B', 'C', 200],
        ['C', 'D', 630],
        ['E', 'D', 80],
        ['F', 'E', 70]
    ]
    print("From city 'A' to 'I' with max stop 5, minimum cost: ", findCheapestPrice(flights, 'A', 'I', 5))
    print("From city 'A' to 'D' with max stop 2, minimum cost: ", findCheapestPrice(flights, 'A', 'D', 2))
    print("From city 'A' to 'D' with max stop 3, minimum cost: ", findCheapestPrice(flights, 'A', 'D', 3))



'''
OUPUT

⚡ /usr/bin/python3 /Users/payalchavan/Documents/Algorithms/Synthesis2/Dijkstras-coding.py
From city 'A' to 'I' with max stop 5, minimum cost:  490
From city 'A' to 'D' with max stop 2, minimum cost:  930
From city 'A' to 'D' with max stop 3, minimum cost:  550
(base)

'''